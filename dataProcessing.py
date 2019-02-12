import numpy as np

class DataProc:
    def __init__(self, baseFilename, OpAmount, ConAmount,Repeat):
        self.baseFilename = baseFilename
        self.OpAmount = OpAmount
        self.ConAmount = ConAmount
        self.Repeat = Repeat

    def open(self):
        self.Data = np.empty([self.OpAmount,self.ConAmount,self.Repeat])
        self.datFn = self.baseFilename + ".txt"
        self.datFile = open(self.datFn, "r")
        op = 0
        con = 0
        re = 0
        # list = []
        for line in self.datFile:
            if op == self.OpAmount:
                op = 0
                re+=1

            line = line.strip()
            self.Data[op][con][re] = float(line)
            con+=1

            if con == self.ConAmount:
                con = 0
                op+=1

    def printOp(self, OpNum):
        if OpNum >= self.OpAmount:
            return "Out of Operator amount"
        else:
            print "Operator-{}: ".format(OpNum)
            for con in range(self.ConAmount):
                print "Connector{0}: {1}".format(con, self.Data[OpNum][con])
                None

    def close(self):
            self.datFile.close()