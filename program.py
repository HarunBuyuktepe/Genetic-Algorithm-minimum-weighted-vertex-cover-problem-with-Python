from Node import Node
import random

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
POP_SIZE = 1
POP_SIZE_MIN = 200
# Maximum, Minimum number of generations the algorithm will run
GEN_NUMBER = 1
GEN_MIN = 100

def generate(number): #population size
    randomList=""
    for i in range(number):
        randomList += str(random.randint(0, 1))
    return randomList

def readFile(path):
    nodeList = []
    edgeList = []
    nodes = 0
    edges = 0
    with open(path) as fp:
        for i, line in enumerate(fp):
            if i == 0:
                nodes = int(line)
            elif i == 1:
                edges = float(line)
            elif i > 1 and i < nodes + 2:
                node = Node(int(line.split()[0]), float(line.split()[1].replace(',', '.')), [])
                nodeList.append(node)
            elif i > nodes + 1:
                f = int(line.split()[0])
                t = int(line.split()[1])
                nodeList[f].getNeighbors().append(nodeList[t])

    return nodeList


def editEdgeMatrix(nodeList, solution): # fill edge matrix
    edgeMatrix = []
    for i in range(len(nodeList)): # create empty adjacency matrix
        edgeMatrix.append(([0 for i in range(len(nodeList))]))

    for i in range(len(nodeList)):
        if(solution[i]=='1'):
            for j in range(len(nodeList[i].getNeighbors())):
                edgeMatrix[i][nodeList[i].getNeighbors()[j].number] = 1
                edgeMatrix[nodeList[i].getNeighbors()[j].number][i] = 1
    return edgeMatrix

def isNotFeasible(solution,nodeList):
    isFeasible = False
    for i in range(len(solution)):
        if solution[i]=='0':
            for j in range(len(nodeList[i].getNeighbors())):
                if solution[nodeList[i].getNeighbors()[j].getNumber()]=='0':
                    return True
    return False


def repair(solution, nodeList):
    print(solution)
    totalFitValue = 0.0
    candidate =[]
    numberOfZeroWeight = 0
    repairedSol = ""
    for i in range(len(nodeList)):
        if (solution[i] == '0'):
            fitnessValue = 0.0
            notVisited = 0
            unvisitedNode = nodeList[i]

            for j in range(len(unvisitedNode.getNeighbors())):
                # print(unvisitedNode.getNeighbors()[j].number)
                if solution[unvisitedNode.getNeighbors()[j].number] == '0':
                    notVisited +=1



            # print(unvisitedNode.getWeight())
            if unvisitedNode.getWeight() ==0:
                unvisitedNode.weight=1
            fitnessValue = notVisited / unvisitedNode.getWeight()


            if fitnessValue != 0:
                if unvisitedNode.getWeight() == 0:
                    totalFitValue+=fitnessValue
                    candidate.append([unvisitedNode, -1])
                else:
                    candidate.append([unvisitedNode,fitnessValue])
    # for i in range(len(candidate)):
    #     print(candidate[i][0].toString()," ",candidate[i][1])
    maxfitness = 0.0
    candi=random.random()
    candidate = sorted(candidate,key=lambda l:l[1], reverse=True)
    # for i in range(len(candidate)):
        # print(candidate[i][0].toString()," ",candidate[i][1])
        # maxfitness = candidate[0][1]
        # print(maxfitness)
    maxfitness = candidate[0][1]

    totalFitValue = totalFitValue + (numberOfZeroWeight * maxfitness)

    if totalFitValue != 0:
       eachPortionSize = 1 / totalFitValue
    else:
        eachPortionSize = 1
    threshold=0
    for c in candidate:
        if threshold + eachPortionSize * c[0].getWeight() > candi:
            # repairedSol = solution
            repairedSol = [char for char in solution]
            print(c[0].getNumber(),"-----------")
            repairedSol[c[0].getNumber()] = '1'
            repairedSol=''.join(repairedSol)
            break
        threshold += eachPortionSize * c[0].getWeight()
    print(repairedSol)
    return repairedSol

if __name__ == "__main__":
    path = "graphs\\003.txt" #TODO:buraya path gelecek
    nodeList = readFile(path)
    solutionList = []
    for i in range(POP_SIZE):#POP_SIZE
        solution = generate(len(nodeList))
        print(solution)
        solutionList.append(solution)
        #adjacency = editEdgeMatrix(nodeList,solution)
        while isNotFeasible(solution, nodeList):
            # print("harun baba")
            solution = repair(solution, nodeList)
        solutionList.append(solution) # actually population
        solutionList.append(solution) # actually population
    GEN_NUMBER = 1 #GEN_MAX
    while GEN_NUMBER != 0:
        print("Number of the generation",GEN_NUMBER)
        for i in range(POP_SIZE):
            print("haryn babuş")

