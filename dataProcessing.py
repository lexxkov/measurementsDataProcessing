import numpy as np

class DataProc:
    def __init__(self, baseFilename, OpAmount, ConAmount):
        self.baseFilename = baseFilename
        self.OpAmount = OpAmount
        self.ConAmount = ConAmount

    def open(self):
        self.datFn = self.baseFilename + ".txt"
        self.datFile = open(self.datFn, "r")
        op = 0
        con = 0
        for line in self.datFile:
            while op < len(self.OpAmount):
                con = 0
                while con < len(self.ConAmount):
                    Data[op,con].append(line)
            op = 0
    def printOp(OpNum=0):
        if OpNum>=len(self.OpAmount):
            return "Out of Operator amount"
        else:
            print "Operator-{}:".format(OpNum)
            for con in self.ConAmount:
                print "Connector-{}: {}".format(con, Data[OpNum,con])

    def close(self):
            self.datFile.close()