def recoverNumber(file):
    numberRecovered = file.readline()
    try:
        value_a = int(numberRecovered)
    except ValueError:
        print("Value found in file isnt a number (might be corrupted)... ")
        exit()
    else:
        return value_a

file1 = open("triangleFile.txt","r+")

base = recoverNumber(file1)

height = recoverNumber(file1)

triangleArea = (base * height)/ 2

print("The area of the triangle is: ", triangleArea)