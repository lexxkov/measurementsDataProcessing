import numpy as np
import matplotlib.pyplot as plt

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
                print "Connector{0}: {1}  Std: {2}".format(con, self.Data[OpNum][con], np.std(self.Data[OpNum][con]))
                None

    def plotOp(self, OpNum):
        fig = plt.figure()
        X = [i for i in range(self.ConAmount)]
        Y = [[self.Data[OpNum][i][j] for i in range(self.ConAmount)] for j in range(self.Repeat)]
        # F = plt.plot(lambda: X,Y[k] for k in range(self.Repeat), 'rx')
        for j in range(self.Repeat):
            plt.plot(X,Y[j], 'gx')
        plt.show()

    def plotCon(self, ConNum):
        fig = plt.figure()
        X = [i for i in range(self.OpAmount)]
        Y = [[self.Data[i][ConNum][j] for i in range(self.OpAmount)] for j in range(self.Repeat)]
        # F = plt.plot(lambda: X,Y[k] for k in range(self.Repeat), 'rx')
        for j in range(self.Repeat):
            plt.plot(X,Y[j], 'gx')
        plt.show()


        # ax = plt.axes([x for x in range(self.ConAmount)], [np.std(self.Data[OpNum][x]) for x in range(self.ConAmount)])
        # ax.plot([], [], lw=2)

    def close(self):
            self.datFile.close()