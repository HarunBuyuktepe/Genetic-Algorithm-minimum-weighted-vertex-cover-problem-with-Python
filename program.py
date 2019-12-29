from Node import Node
from Edge import Edge
import numpy as np
import sys

def generate(nodeList,number):
    to=len(nodeList)
    # randomList = np.random.uniform(0,1,100)
    randomList=np.zeros((2, 3))
    # print(randomList)


# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

# tokens = (str(sys.argv).replace('\'','').replace(',','').replace(']','').split())
# if len(tokens)==6:
#     print('Name of the graph file ',tokens[1])
#     print('Number of generations ',tokens[2])
#     print('Population size ',tokens[3])
#     print('Crossover probability ',tokens[4])
#     print('Mutation probability ',tokens[5])
# else:
#     print("Wrong Format")

path="graphs\\003.txt"

nodeList=[]
edgeList=[]
nodes=0
edges=0
with open(path) as fp:
    for i, line in enumerate(fp):

        if i == 0:
            # print(line)
            nodes=int(line)
        elif i == 1:
            # print(line)
            edges=float(line)
        elif i > 1 and i<nodes+2:
        #     print(line)
            node = Node(int(line.split()[0]),float(line.split()[1].replace(',','.')))
            nodeList.append(node)
        elif i > nodes+1:
            #print(line)
            edge = Edge(int(line.split()[0]),int(line.split()[1]))
            edgeList.append(edge)

# print(nodeList[1].toString())
# print(nodeList[1].getWeight())
# print(edgeList[1].toString())
# print(edgeList[1].getEnd())
print(len(edgeList))


generate(nodeList,100)


