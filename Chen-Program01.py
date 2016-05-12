#Alex Chen,CSC201
#Lab 01

#Part 1
#Objective: To make a half pyramid.

#This statement is asking user to input a number for the levels.
levels = int(input("How many levels?:"))
blocks = input("Choose a building block:")
for i in range(levels):
    print(blocks+(i*blocks))
input("Press Enter to continue.")



#Part 2
#Objective: To make a full pyramid

#This statement is asking user to input a number for the levels.
levels = int(input("How many levels?:"))
#This statement is asking user to input a block for the pyramid.
blocks = input("Choose a building block:")
for j in range(levels):
#This line prints out the half pryamid.
    print(((levels-j)*" ")+(2*j+1)*blocks)

input("Press Enter to continue.")



#Part 3
#Objective: To fix the problem of adding a string of 2 characters or more.

#This statement is asking user to input a number for the levels.
levels = int(input("How many levels: "))
#This statement is asking user to input a block for the pyramid.
blocks = input("Choose a building block:")
n = len(blocks)
for k in range(levels):
#This line prints out the half pryamid.
    print(((levels-k)*n*" ")+(2*k+1)*blocks)

input("Press Enter to continue.")



#Part 4

#Objective: To make a parabola.
#This line is asking the user to input the mini. value for x.
min_val = int(input("Enter the minimum value:"))
#This line is asking the user to input the maxi. value for x.
max_val = int(input("Enter the maximum value:"))
#This line is asking the user to input the scaling factor for the parabola.
scal_fac = float(input("Enter the scaling factor:"))
#This is putting the mini. value into a variable.
a = min_val
while a <= max_val:
    b = scal_fac*(a ** 2)
    print((int(b-1)*" ")+("*"))
    a += 1
    
input("Press Enter to continue.")



#Part 5
#Objective: To make a circle.

#This is asking the user to enter the value and putting it into the variable "radius".
radius = int(input("Enter the radius:"))

for i in range(radius):
    k = ((radius ** 2)-((radius-i) ** 2)) ** 0.5
    print((int(radius-k)*" ")+("*")+(int(k*2)*" ")+("*"))
for j in range(radius):
    k = ((radius ** 2)-((j) ** 2)) ** 0.5
    print((int(radius-k)*" ")+("*")+(int(k*2)*" ")+("*"))

#End of program 1.



