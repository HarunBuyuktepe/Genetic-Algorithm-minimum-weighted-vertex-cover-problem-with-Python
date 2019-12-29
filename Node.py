class Node:
    def __init__(self, number, weight):
        self.number = number
        self.weight = weight
    def getWeight(self):
        return self.weight
    def getNumber(self):
        return self.number
    def toString(self):
        return str(self.number)+" "+str(self.weight)