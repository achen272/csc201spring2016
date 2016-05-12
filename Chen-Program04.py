#Alex Chen,CSC201
#Program04

import sys

#Part1

expr = input("Enter the expression:")
def simpleExpressionIsValid(expr):
        opers = set(["+", "-", "*", "/"])
        for i in opers:
            if i in expr:
                index = expr.find(i)
                num1 = expr[0:index]
                num2 = expr[index+1:]
                if num1.isdigit() and num2.isdigit():
                    return True
                else:
                    return False
                return expr
print(simpleExpressionIsValid(expr))

input("Press enter to continue")

#Part2

expr = input("Enter the expression:")
def evaluateSimpleExpression(expr):
    result = eval(expr)
    return result
print(evaluateSimpleExpression(expr))

input("Press enter to continue")

#Part3

def evaluateSimpleExpression(expr):
    result = eval(expr)
    return result

def simpleExpressionIsValid(expr):
        opers = set(["+", "-", "*", "/"])
        for i in opers:
            if i in expr:
                index = expr.find(i)
                num1 = expr[0:index]
                num2 = expr[index+1:]
                if num1.isdigit() and num2.isdigit():
                    return True
                else:
                    return False
                return expr

#-------------------------------------------------------------------------------
#Main
                
def main():
        expr = input("Enter the expression:")
        if expr == "end":
                print("Exit")
                sys.exit(0)

        if simpleExpressionIsValid(expr):
                print(expr + "=" + str(evaluateSimpleExpression(expr)))
        else:
                print("Invalid expression")

while(True):
        main()

input("Press enter to continue")

#Part4

def run():
    expr = input("Enter the expression:")
    if expr == "end":
            print("Exit")
            sys.exit(0)

    if simpleExpressionIsValid(expr):
        print(expr + "=" + str(evaluateSimpleExpression(expr)))

    elif expr == "List":
        print(infiniteMem(expression))

    else:
        print("Invalid expression")

def infiniteMem(expression):
    myList = []
    [myList.append(x) for x in expression if x not in myList]
    return myList

expression = input("Enter the expression:")
expression = ' '.join(infiniteMem(expression.split()))
print(expression)
    
def evaluateSimpleExpression(expr):
    result = eval(expr)
    return result

def simpleExpressionIsValid(expr):
        opers = set(["+", "-", "*", "/"])
        myList = []
        for i in opers:
            if i in expr:
                index = expr.find(i)
                num1 = expr[0:index]
                num2 = expr[index+1:]
                if num1.isdigit() and num2.isdigit():
                    return True
                    myList.append(expr)
                else:
                    return False
                return expr

#-------------------------------------------------------------------------------
#Main

while(True):
    run()

input("Press enter to continue")

#Part5

def evaluateComplexExpression():
        expr = input("Enter the expression:")
        opers = set(["+", "-", "*", "/"])
        paren = set(["(",")"])
        if expr == "end":
            print("Exit")
            sys.exit(0)
        for j in paren:
            parenthese = expr.find(j)
            paren1 = expr[0]
            paren2 = expr[6]
            paren3 = expr[12]
            paren4 = expr[4]
            paren5 = expr[10]
            paren6 = expr[16]
            
        for i in opers:
            if i in expr:
                index = expr.find(i)
        num1 = expr[1]
        num2 = expr[7]
        num3 = expr[13]
        num4 = expr[3]
        num5 = expr[9]
        num6 = expr[15]
        valid = True
        if num1.isdigit() and num2.isdigit() and num3.isdigit() and num4.isdigit() and num4.isdigit() and num5.isdigit() and num6.isdigit():
                valid == True
                result = eval(expr)
        else:
                valid == False
                result = "?"
                print("Invalid expression")
        print(str(expr)+ "=" + str(result))

while(True):
    evaluateComplexExpression()

input("Press enter to continue")

#Part6

def evaluateComplexExpression2():
        expr = input("Enter the expression:")
        opers = set(["+", "-", "*", "/"])
        paren = set(["(",")"])
        if expr == "end":
            print("Exit")
            sys.exit(0)
        for j in paren:
            parenthese = expr.find(j)
            paren1 = expr[0]
            paren2 = expr[6]
            paren3 = expr[12]
            paren4 = expr[4]
            paren5 = expr[10]
            paren6 = expr[16]
            
        for i in opers:
            if i in expr:
                index = expr.find(i)
        num1 = expr[1]
        num2 = expr[7]
        num3 = expr[13]
        num4 = expr[3]
        num5 = expr[9]
        num6 = expr[15]
        valid = True
        if num1.isdigit() and num2.isdigit() and num3.isdigit() and num4.isdigit() and num4.isdigit() and num5.isdigit() and num6.isdigit():
                valid == True
                result = eval(expr)
        else:
                valid == False
                result = "?"
                print("Invalid expression")
        print(str(expr)+ "=" + str(result))

while(True):
    evaluateComplexExpression2()
