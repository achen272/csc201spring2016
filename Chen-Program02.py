#Alex Chen,CSC201
#Lab 02

import re
import sys

def run():
    expr = input("Enter the expression:")
    num = re.split("\D", expr)
    if expr == "Q":
        print("Exit")
        sys.exit(0)
        
    x = checkInfo(num)
    if x == True:
         invalid()
    else:
        math(expr, num)

def invalid():
    print("Invalid")
    run()

def checkInfo(num):
    for x in num:
        if x == "" or len(num) == 1:
            return True 

def math(expr, num):
    
     oper = expr.find("+")
     if oper != -1:
        result = int(num[0]) + int(num[1])
        print(expr + " = " + str(result))
    
     oper = expr.find("-")
     if oper != -1:
        result = int(num[0]) - int(num[1])
        print(expr + " = " + str(result))

     oper = expr.find("*")
     if oper != -1:
        result = int(num[0]) * int(num[1])
        print(expr + " = " + str(result))
        
     oper = expr.find("/")
     if oper != -1:
        result = int(num[0]) / int(num[1])                   
        print(expr + " = " + str(result))
     
while (True):
    run()








