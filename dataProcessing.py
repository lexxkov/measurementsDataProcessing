import numpy as np
import matplotlib.pyplot as plt
import os

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

    def saveplot(self, name=''):
        pwd = os.getcwd()
        iPath = './pictures'
        if not os.path.exists(iPath):
            os.mkdir(iPath)
        os.chdir(iPath)
        plt.savefig('{}.{}'.format(name, 'png'))
        os.chdir(pwd)

    def plotOp(self, OpNum, Show=False, Save=False):
        fig = plt.figure()
        plt.title('Operator{}'.format(OpNum))
        plt.ylabel('Value, a.u.')
        plt.xlabel('Connector Number')
        ax = fig.add_subplot(111)
        X = np.arange(self.ConAmount)
        Y = [[self.Data[OpNum][i][j] for i in range(self.ConAmount)] for j in range(self.Repeat)]

        Txt=''
        for i in range(self.ConAmount):
            Txt=Txt+"Std{0}: {1:.5f}\n".format(i, np.std(self.Data[OpNum][i]))

        ax.text(0.99, 0.74, Txt, fontsize=10, transform=ax.transAxes, horizontalalignment='right', verticalalignment='center', bbox=dict(facecolor='white', alpha=0.5))

        for j in range(self.Repeat):
            plt.plot(X,Y[j], 'gx')
        if Save:
            name = 'Operator{}'.format(OpNum)
            self.saveplot(name)
        if Show:
            plt.show()

    def plotCon(self, ConNum,Show=False, Save=False):
        fig = plt.figure()
        plt.title('Connector{}'.format(ConNum))
        plt.ylabel('Value, a.u.')
        plt.xlabel('Operator Number')
        plt.axis(xmin=-0.1, xmax=self.OpAmount)
        ax = fig.add_subplot(111)
        X = np.arange(self.OpAmount)
        print X
        Y = [[self.Data[i][ConNum][j] for i in range(self.OpAmount)] for j in range(self.Repeat)]
        ax.set_xticks(X, minor=False)

        for j in range(self.Repeat):
            plt.plot(X,Y[j], 'gx')
        Txt=''
        for i in range(self.OpAmount):
            Txt=Txt+"Std{0}: {1:.5f}\n".format(i, np.std(self.Data[i][ConNum]))

        ax.text(0.99, 0.9, Txt, fontsize=10, transform=ax.transAxes, horizontalalignment='right', verticalalignment='center', bbox=dict(facecolor='white', alpha=0.5))

        if Save:
            name = 'Connector{}'.format(ConNum)
            self.saveplot(name)

        if Show:
            plt.show()

    def close(self):
            self.datFile.close()