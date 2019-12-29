class Edge:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    def getEnd(self):
        return self.end
    def getBegin(self):
        return self.begin
    def toString(self):
        return str(self.begin)+" "+str(self.end)