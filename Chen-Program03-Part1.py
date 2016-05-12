#Alex Chen,CSC201
#Lab03,Part1
#Objective:Computing mirrors of DNA sequences

DNA = input("Enter the DNA sequence:")
newDNA = ""
for i in DNA:
    if i == "A":
        newDNA += "T"
    elif i == "T":
        newDNA += "A"
    elif i == "C":
        newDNA += "G"
    elif i == "G":
        newDNA += "C"
    else:
        print("Invalid input")

print(newDNA)

input("Press enter to continue:")

#Lab03,Part2
#Objective:Reversing the string of DNA sequences

DNA = input("Enter the DNA sequence:")
print(DNA[::-1])

input("Press enter to continue:")

#Lab03,Part3
#Objective:Verifying validity of DNA sequences

Valid_DNA = "A,G,C,T"
DNA = input("Enter the DNA sequence:")

valid = True
for i in DNA:
    if i not in Valid_DNA:
        valid = False
        break

if valid == True:
    print("This is a valid DNA sequence")
else:
    print("This is an invalid DNA sequence")

input("Press enter to continue:")

#Lab03,Part4
#Objective:Basic equality matches of two DNA sequences

Valid_DNA = "A,G,C,T"
DNA1 = input("Enter the first DNA sequence:")
DNA2 = input("Enter the second DNA sequence:")

newDNA = ""
for k in DNA1:
    if k == "A":
        newDNA += "T"
    if k == "T":
        newDNA += "A"
    if k == "C":
        newDNA += "G"
    if k == "G":
        newDNA += "C"

newDNA2 = ""
for y in DNA2:
    if y == "A":
        newDNA2 += "T"
    if y == "T":
        newDNA2 += "A"
    if y == "C":
        newDNA2 += "G"
    if y == "G":
        newDNA2 += "C"

valid = True
for i in DNA1:
    if i not in Valid_DNA:
        valid = False
        break

if valid == True:
    print("The first DNA sequence is valid")
    print("DNA1 Mirror:",newDNA)
    print("DNA1 Reverse:",DNA1[::-1])
else:
    print("The first DNA sequence is invalid")

newDNA = DNA1[::-1]

if sorted(newDNA.split()) == sorted(DNA1[::-1].split()):
    print("Both DNA's represent the same fragments")
else:
    print("Does not represent the same DNA fragments")

print("\n")

valid = True
for j in DNA2:
    if j not in Valid_DNA:
        valid = False
        break

if valid == True:
    print("The second DNA sequence is valid")
    print("DNA1 Mirror:",newDNA)
    print("DNA1 Reverse:",DNA1[::-1])
else:
    print("The second DNA sequence is invalid")

newDNA2 = DNA2[::-1]

if sorted(newDNA2.split()) == sorted(DNA2[::-1].split()):
    print("Both DNA's represent the same fragments")
else:
    print("Does not represent the same DNA fragments")
