class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    def getWeight(self):
        return self.weight
    def getValue(self):
        return self.value
    def toString(self):
        return str(self.value)+" "+str(self.weight)