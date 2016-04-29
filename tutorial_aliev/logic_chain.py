#!/usr/bin/python3


class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.perfomGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input('Enter Pin A input for gate' + self.getLabel() + '-->'))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input('Enter Pin B input for gate' + self.getLabel() + '-->'))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('Error: NO EMPTY PINS')


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        return int(input('Enter Pin input for gate' + self.getLabel() + '-->'))


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def perfomGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        togate.setNextPin(self)

    def getFrom(self):
        return self.formgate

    def getTo(self):
        return self.togate


g1 = AndGate('G1')
print(g1.perfomGateLogic())
