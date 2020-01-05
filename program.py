from Node import Node
from Edge import Edge
import numpy as np
import random
import sys

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

# Size of initial population filled with some permutation of 0s and 1s
POP_SIZE = 200
POP_SIZE_MIN = 100
# Maximum, Minimum number of generations the algorithm will run
GEN_MAX = 400
GEN_MIN = 100

def generate(number): #popuşation size
    randomList = [random.randint(0, 1) for x in range(0, number)]
    # randomList = np.random.uniform(0,1,100)
    # # randomList=np.zeros((2, 3))
    # # print(randomList)
    # print(randomList)
    return randomList

def readFile(path):
    nodeList = []
    edgeList = []
    nodes = 0
    edges = 0
    with open(path) as fp:
        for i, line in enumerate(fp):
            if i == 0:
                # print(line)
                nodes = int(line)
            elif i == 1:
                # print(line)
                edges = float(line)
            elif i > 1 and i < nodes + 2:
                # print(line)
                node = Node(int(line.split()[0]), float(line.split()[1].replace(',', '.')))
                nodeList.append(node)
            elif i > nodes + 1:
                # print(line)
                f = int(line.split()[0])
                t = int(line.split()[1])
                if len(edgeList) == 0:
                    edge = Edge(f, t)
                    edgeList.append(edge)
                    continue
                for e in edgeList:
                    if (e.getBegin() != f and e.getEnd() != t) or (e.getBegin() != t and e.getEnd() != f):
                        edge = Edge(f, t)
                        edgeList.append(edge)
                        break

            # print(nodeList[1].toString())
            # print(nodeList[1].getWeight())
            # print(edgeList[1].toString())
            # print(edgeList[1].getEnd())
    return nodeList,edgeList


if __name__ == "__main__":
    path = "graphs\\003.txt" #TODO:buraya path gelecek
    nodeList,edgeList = readFile(path)
    # print("uzunluğu",len(nodeList))
    # for node in nodeList:
    #     print(node.toString())
    # print("uzunluğu", len(edgeList))
    # for edge in edgeList:
    #     print(edge.toString())
    print(len(edgeList))

    generation=1
    # for g in range(0, GEN_MAX):
    #     randomList = generate(1000)
    #     print("Generation %d with population size %d" % (generation, len(randomList)))
    #     print(randomList)
    #     generation+=1


