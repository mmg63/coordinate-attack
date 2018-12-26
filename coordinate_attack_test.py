from NODES import Node
from time import time


startTime = time()

def test(priviLegeLevel = False, printMessageContent = False):
    node1 = Node(1, 3, 20, priviLegeLevel, True)
    node2 = Node(2, 3,20, priviLegeLevel)
    node3 = Node(3, 3, 20, priviLegeLevel)
    print("Node 1 initial value:\n", node1.getState_i())
    print("Node 2 initial value:\n", node2.getState_i())
    print("Node 3 initial value:\n", node3.getState_i())
    print("===============================")

    #   1st broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)

    #   2nd broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)

    #   3rd broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)

    #   4th broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)

    #   5th broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)
    #   6th broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)
    #   7th broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)
    #   8th broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)
    #   9th broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)
    #   10th broadcast
    node2.setState_j(node1.getState_i(), 1)
    node3.setState_j(node1.getState_i(), 1)
    node1.setState_j(node2.getState_i(), 2)
    node3.setState_j(node2.getState_i(), 2)
    node1.setState_j(node3.getState_i(), 3)
    node2.setState_j(node3.getState_i(), 3)

    if printMessageContent:
        print("node 1 matrix final value : \n", node1.getState_i())
        print("node 2 matrix final value: \n", node2.getState_i())
        print("node 3 matrix final value: \n", node3.getState_i())

    #
    print("\nNode 1 Consensus Answer:  ", node1.consensus(node1.getState_i(), 1))
    print("\nNode 2 Consensus Answer:  ", node2.consensus(node2.getState_i(), 2))
    print("\nNode 3 Consensus Answer:  ", node3.consensus(node3.getState_i(), 3))


for i in range(1,2):
    print(test(False, True))

endTime = time()
print('Estimated time is ', endTime - startTime)
