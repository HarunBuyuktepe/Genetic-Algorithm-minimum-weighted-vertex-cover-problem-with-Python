class Node:
    neighbors=[]
    def __init__(self, number, weight, neighbors):
        self.number = number
        self.weight = weight
        self.neighbors = neighbors
    def getWeight(self):
        return self.weight
    def getNumber(self):
        return self.number
    def getNeighbors(self):
        return self.neighbors
    def toString(self):
        nei=""

        for ne in self.neighbors:
            nei = nei+" \n\t"+str(ne.number)+" "+str(ne.weight)

        return str(self.number)+" "+str(self.weight)+" "+nei