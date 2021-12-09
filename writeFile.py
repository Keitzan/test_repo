def numberInserter(file):
    boolCheck = False
    while(boolCheck == False):
        functionNumber = input("Insert a number ")
        try:
            value_a = int(functionNumber)
        except ValueError:
            print("Thats not a number! Try again... ")
        else:
            print("Number inserted correctly")
            file.write(functionNumber + "\n")
            boolCheck = True    


file1 = open("triangleFile.txt","w")
#Inserting first number
numberInserter(file1)
#Inserting first number
numberInserter(file1)
