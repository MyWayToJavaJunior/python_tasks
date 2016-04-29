#!/usr/bin/python3

# если "верхняя" граница справа, а основание слева


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return self.items


s = Stack()
s.push(1)
# print(s)
# print(s.isEmpty())
#
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())


# если "верхняя" граница слева, а основание справа
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s = Stack()
s.push('hello')
s.push('true')
print(s.pop())
"""


def revstring(mystr):
    myStack = Stack()

    for ch in mystr:
        myStack.push(ch)

    revstr = ''
    while not myStack.isEmpty():
        revstr += myStack.pop()

    return revstr

# print(revstring('apple'))


# реализация мини "интерпретатора"

def parChecker(symbolString):

    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:

        symbol = symbolString[index]

        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

# print(parChecker('((()))'))
# print(parChecker('(()'))
# print(parChecker('((('))
# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))


# из 10 в 2
def divideBy2(decNumber):

    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not remStack.isEmpty():
        binString += str(remStack.pop())

    return binString

# print(divideBy2(42))


# из 10 в (от 2 до 16)
def baseConverter(decNumber, base):

    digits = '0123456789ABCDEF'
    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remStack.isEmpty():
        newString += digits[remStack.pop()]

    return newString

# print(baseConverter(25,2))
# print(baseConverter(25,16))
# print(baseConverter(25,8))
# print(baseConverter(26,26))

# из инфиксного в постфиксного


def infixToPostfix(infixexpr):
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ' '.join(postfixList)

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(infixToPostfix("( A + B ) * ( C + D )"))
# print(infixToPostfix("( A + B ) * C"))
# print(infixToPostfix("A + B * C"))
# print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))


# постфиксное

def post_fix_eval(post_fix):
    operand_stack = Stack()
    token_list = post_fix.split()

    for token in token_list:
        if token in '0123456789':
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2

# print(post_fix_eval('7 8 + 3 2 + /'))
