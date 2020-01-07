from Node import Node
import random
import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

tokens = (str(sys.argv).replace('\'','').replace(',','').replace(']','').split())
if len(tokens)==7:
    print('Name of the graph file ',tokens[2])
    print('Number of generations ',tokens[3])
    print('Population size ',tokens[4])
    print('Crossover probability ',tokens[5])
    print('Mutation probability ',tokens[6])
else:
    print("Wrong Format")
Filename=tokens[2]
# Size of initial population filled with some permutation of 0s and 1s
POP_SIZE = int(tokens[4])
# Maximum, Minimum number of generations the algorithm will run
GEN_NUMBER = int(tokens[3])
GEN_NUMBER1= int(tokens[3])
# crossoverProbability
CROSSOVER = float(tokens[5])
# Mutasyon
MUTATIONPROB =tokens[6]
print(Filename," ", GEN_NUMBER," ",POP_SIZE," ",CROSSOVER," ",MUTATIONPROB)
def generate(number): #population size
    randomList=""
    for i in range(number):
        randomList += str(random.randint(0, 1))
    return randomList

def readFile(path):
    nodeList = []
    nodes = 0
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

def isNotFeasible(solution,nodeList):
    for i in range(len(solution)):
        if solution[i]=='0':
            for j in range(len(nodeList[i].getNeighbors())):
                if solution[nodeList[i].getNeighbors()[j].getNumber()]=='0':
                    return True
    return False

def repair(solution, nodeList):
    # print(solution)
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

    maxfitness = 0.0
    candi=random.random()
    candidate = sorted(candidate,key=lambda l:l[1], reverse=True)
    maxfitness = candidate[0][1]

    totalFitValue = totalFitValue + (numberOfZeroWeight * maxfitness)

    if totalFitValue != 0:
       eachPortionSize = 1 / totalFitValue
    else:
        eachPortionSize = 1
    threshold=0
    for c in candidate:
        if threshold + eachPortionSize * c[0].getWeight() > candi:
            repairedSol = [char for char in solution]
            repairedSol[c[0].getNumber()] = '1'
            repairedSol=''.join(repairedSol)
            break
        threshold += eachPortionSize * c[0].getWeight()
    # print(repairedSol)
    return repairedSol

def getFitnessValue(solution, nodeList):
    oneNumber = 0
    totalWeight = 0.0

    for i in range(len(solution)):
        if solution[i] == '1':
            oneNumber +=1
            totalWeight += nodeList[i].getWeight()
    if totalWeight != 0:
        return oneNumber / totalWeight
    else: return 1
def selectSolution(solutionList, nodeList):
    totalFitnessValue = 0.0
    fitnessValues = []

    for i in range(len(solutionList)):
        fitnessValues.append(getFitnessValue(solutionList[i], nodeList))
        totalFitnessValue += fitnessValues[i]

    candi = random.random()
    if totalFitnessValue != 0:
       eachPortionSize = 1 / totalFitnessValue
    else:
        eachPortionSize = 1
    fitnessValues = sorted(fitnessValues,key=float, reverse=True)

    parent = ""
    threshold = 0.0

    for i in range(len(solutionList)):
        if threshold + eachPortionSize * fitnessValues[i] > candi:
            parent = solutionList[i]
            break
        threshold += eachPortionSize*fitnessValues[i]

    return parent

def getTotalWeight(solution,nodeList):
    total = 0.0
    for i in range(len(solution)):
        if(solution[i]=='1'):
            total += nodeList[i].getWeight()

    return total

if __name__ == "__main__":

    path = "graphs\\"+Filename #TODO:buraya path gelecek
    nodeList = readFile(path)
    solutionList = []
    CrossOverPopulation = []
    MutationPopulation = []
    bestSolutions = []

    if tokens[6] == "1/n":
        MUTATIONPROB = 1 / len(nodeList)
    else:
        MUTATIONPROB = float(tokens[5])
    print("Initial population is creating")
    print("Initial population is repairing")
    for i in range(POP_SIZE):#POP_SIZE
        solution = generate(len(nodeList))
        while isNotFeasible(solution, nodeList):
            solution = repair(solution, nodeList)
        solutionList.append(solution) # actually population



    matching_pool = []
    while GEN_NUMBER != 0:
        print("Number of the generation ",GEN_NUMBER1 - GEN_NUMBER)
        for i in range(POP_SIZE):
            matching_pool.append(selectSolution(solutionList,nodeList))


        for k in range(int(len(solutionList)/2)):
            firstParent = selectSolution(matching_pool,nodeList)
            secondParent = selectSolution(matching_pool,nodeList)

            crossoverdecisionmaker = random.random()
            if(crossoverdecisionmaker<CROSSOVER):
                crossoverPoint = int(random.random()*len(matching_pool))
                firstChild = firstParent[:crossoverPoint]+secondParent[crossoverPoint:]
                secondChild = secondParent[:crossoverPoint]+firstParent[crossoverPoint:]
                CrossOverPopulation.append(firstChild)
                CrossOverPopulation.append(secondChild)
            else:
                CrossOverPopulation.append(firstParent)
                CrossOverPopulation.append(secondParent)


        for m in range(len(CrossOverPopulation)):
            mutation = [char for char in CrossOverPopulation[m]]
            for n in range(len(mutation)):
                mutat = random.random()
                if mutat < MUTATIONPROB:
                    if mutation[n] == '1':
                        mutation[n] = '0'
                    else:
                        mutation[n] = '1'
            mutation = ''.join(mutation)
            MutationPopulation.append(mutation)


        for i in range(len(MutationPopulation)):  # POP_SIZE
            while isNotFeasible(MutationPopulation[i], nodeList):
                MutationPopulation[i] = repair(MutationPopulation[i], nodeList)

        solutionList.clear()
        matching_pool.clear()
        CrossOverPopulation.clear()
        solutionList= MutationPopulation.copy()

        x = -1
        max = -1
        for i in range(len(MutationPopulation)):
            if max<getFitnessValue(MutationPopulation[i],nodeList):
                max =getFitnessValue(MutationPopulation[i],nodeList)
                x = i
        bestSolutions.append(MutationPopulation[x])
        MutationPopulation.clear()
        GEN_NUMBER -=1
    x = -1
    max = -1
    for i in range(len(bestSolutions)):
        if max < getFitnessValue(bestSolutions[i], nodeList):
            max = getFitnessValue(bestSolutions[i], nodeList)
            x = i
    wrtFile = str(Filename)+str(GEN_NUMBER1)+str(POP_SIZE)+str(CROSSOVER)+str(MUTATIONPROB)+"txt"
    file1 = open(wrtFile, "w")
    for k in range(len(bestSolutions)):
        strt = '' + str(k) + " " + str(getTotalWeight(bestSolutions[k], nodeList)) + "\n"
        file1.write(strt)
    file1.close()
    bestofbest = bestSolutions[x]
    print("Output of the system ")
    print(bestofbest)
    print()
    print("Graph Name is ",Filename)
    print("Generation size is ",GEN_NUMBER)
    print("Population size is ",POP_SIZE)
    print("Crossover probability is ",CROSSOVER)
    print("Mutation probability is ",MUTATIONPROB)
    print("The best solution is ", getTotalWeight(bestofbest,nodeList))


