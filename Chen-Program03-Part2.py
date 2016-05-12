#Alex Chen,CSC201
#Lab03,Part5
#Objective:Computing the total number of matching DNA fragments

DNA1 = input("Enter the first DNA sequence:")
DNA2 = input("Enter the second DNA sequence:")

def dna_Match(DNA1,DNA2):
    count = 0
    if len(DNA1) > len(DNA2):
        small = DNA2
        big = DNA1
    else:
        small = DNA1
        big = DNA2

    for i in range(len(small)):
        if small[i] == big[i]:
            count += 1
    return count
print(dna_Match(DNA1,DNA2))

input("Press enter to continue:")

#Lab03,Part6
#Objective:Computing the length of the longest matching DNA fragments

DNA1 = input("Enter the first DNA sequence:")
DNA2 = input("Enter the second DNA sequence:")

def dna_Length(DNA1,DNA2):
        count = 0
        maxMatch = 0
        if len(DNA1) > len(DNA2):
            small = DNA2
            big = DNA1
        else:
           small = DNA1
           big = DNA2

        for i in range(len(small)):
                if small[i] == big[i]:
                        count += 1
                else:
                        count = 0
                if count > maxMatch:
                        maxMatch = count
        return maxMatch
print(dna_Length(DNA1,DNA2))

input("Press enter to continue:")

#Lab03,Part7
#Objective:Complete DNA search

def validate(dna_Frag): 
    valid = True
    for i in dna_Frag:
        if i not in Valid_DNA:
            valid = False
            break
    return valid

def dna_Match(dna_Frag,gene):
    count = 0
    if len(dna_Frag) > len(gene):
        small = gene
        big = dna_Frag
    else:
        small = dna_Frag
        big = gene

    for i in range(len(small)):
        if small[i] == big[i]:
            count += 1
    return count

def compare(matchList):
    gList = ""
    greatest = matchList[0]
    if matchList[1] > greatest:
        greatest = matchList[1] 
    elif matchList[2]  > greatest:
        greatest = matchList[2] 
    elif matchList[3]  > greatest:
        greatest = matchList[3] 

    for i in range(len(matchList)):
        if matchList[i] == greatest:
            gList += ("Gene" + str(i + 1) + " ")
    return gList

def len_Compare(lengthList):
    lList = ""
    greatest = lengthList[0]
    if lengthList[1] > greatest:
        greatest = lengthList[1] 
    elif lengthList[2]  > greatest:
        greatest = lengthList[2] 
    elif lengthList[3]  > greatest:
        greatest = lengthList[3] 

    for i in range(len(lengthList)):
        if lengthList[i] == greatest:
            lList += ("Gene" + str(i + 1) + " ")
    return lList

def dna_Length(dna_Frag,gene):
        count = 0
        maxMatch = 0
        if len(dna_Frag) > len(gene):
            small = gene
            big = dna_Frag
        else:
           small = dna_Frag
           big = gene

        for i in range(len(small)):
                if small[i] == big[i]:
                        count += 1
                else:
                        count = 0
                if count > maxMatch:
                        maxMatch = count
        return maxMatch

################################################################################
#Main:

Valid_DNA = "AGCT"
gene1 = "ATTAGGTAA"
gene2 = "ACTGATCAG"
gene3 = "ATTCGGCTC"
gene4 = "TAGCCGTTA"

dna_Frag = input("Enter the DNA sequence:")
isValid = validate(dna_Frag)

while isValid == False:
    print("Invalid entry")
    dna_Frag = input("Renter the DNA sequence:")
    isValid = validate(dna_Frag)

gene1match = dna_Match(dna_Frag, gene1)
gene2match = dna_Match(dna_Frag, gene2)
gene3match = dna_Match(dna_Frag, gene3)
gene4match = dna_Match(dna_Frag, gene4)

matchList = [gene1match, gene2match, gene3match, gene4match]
gList = compare(matchList)

print("The best matches are:",gList)

gene1length = dna_Length(dna_Frag, gene1)
gene2length = dna_Length(dna_Frag, gene2)
gene3length = dna_Length(dna_Frag, gene3)
gene4length = dna_Length(dna_Frag, gene4)

lengthList = [gene1length, gene2length, gene3length, gene4length]
lList = len_Compare(lengthList)

print("The longest consecutive matches are:",lList)
