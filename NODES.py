import numpy as np
from random import randint

# from random import randint, choice
# maxIteration is specifed to the maximum number of send and receive packets in program.
# numberOfNodes is specified to number of nodes inside the network.
#  isFirstNode is specified to which node is the first node; The purpose of specifying this property is
#  for creating random number for consensus.

class Node:
    def __init__(self, uid, numberOfNodes, maxRound, privilegeLevel = False, isFirstNode = False):
        self._numberOfNodes = numberOfNodes + 1
        self.maxRound = maxRound
        self._uid = uid
        self._isFirstNode = isFirstNode
        self.round = -1
        self.privilegeLevel = privilegeLevel # set own opinion value to One
        # row 0 is nodes information level [0,1,unkown]
        # row 1 is nodes value [0,1]
        # row 2 is nodes key value [1..r)
        # -1 means unknown
        self.nodeStatus = np.zeros((3, self._numberOfNodes))
        for i in range(self._numberOfNodes):
            self.nodeStatus[0][i] = -1 #own information level
            self.nodeStatus[1][i] = -1 #node j value
            self.nodeStatus[2][i] = -1 #key value

        self.nodeStatus[0][self._uid] = -1

        if privilegeLevel:
            self.nodeStatus[1][self._uid] = 1
        else:
            self.nodeStatus[1][self._uid] = randint(0, 1)

        if isFirstNode and self.round == -1:
            self.nodeStatus[2][self._uid] = randint(1, self.maxRound)

    def getState_i(self):
        return self.nodeStatus

    def setState_j(self, nodeState_j, ruID):

        self.round += 1

        ownLevel = self.nodeStatus[0][self._uid]
        min_level = 100
        for i in range(1, self._numberOfNodes):
            self.nodeStatus[0][i] = max(nodeState_j[0][i],
                                        self.nodeStatus[0][i])#update level other information

            min_level = min(min_level, self.nodeStatus[0][i]) #calculate the minimun level

            if self.nodeStatus[1][i] == -1:#     valid       update value of the nodes
                self.nodeStatus[1][i] = nodeState_j[1][i]

                if nodeState_j[2][i] != -1:  # valid       update key of the nodes
                    self.nodeStatus[2][i] = nodeState_j[2][i]

        self.nodeStatus[0][ruID] = 1 + min(min_level, ownLevel) # update message own level information

        # store key to the message i if its node uid isn't 1
        self.nodeStatus[2][self._uid] = max(nodeState_j[2][1],
                                            self.nodeStatus[2][1])


    def consensus(self, nodeState_j,uID):

        val_j = 0
        for i in range(2, self._numberOfNodes):
            val_j = min(nodeState_j[1][i - 1], nodeState_j[1][i])
        if ((nodeState_j[2][uID] != -1) and # if key is not null
                (nodeState_j[0][uID] >= nodeState_j[2][uID]) and # if information level is greater than the key
                (val_j == 1)): # if all node value is true to attack
            return True
        else:
            return False
