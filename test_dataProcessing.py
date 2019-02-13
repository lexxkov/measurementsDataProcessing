from dataProcessing import *
OperatorAmount = 3
ConnectorAmount = 10
SavePlot=True
ShowPlot=False
Repeat = 3
Operator1=0
Operator2=1
Operator3=2
filePath = '/home/alex/PythonTasks/measurementsDataProcessing/RAW/data'
Data = DataProc(filePath, OperatorAmount , ConnectorAmount, Repeat)
Data.open()
Data.printOp(Operator1)
Data.printOp(Operator2)
Data.printOp(Operator3)
Data.plotCon(0, True, False)
for i in range(OperatorAmount):
    Data.plotOp(i, ShowPlot, SavePlot)
for i in range(ConnectorAmount):
    Data.plotCon(i, ShowPlot, SavePlot)
Data.close()