# ACTIVITY 1

'''def my_firstfunct(arg1, arg2):
    total = arg1 + arg2
    return total

print(my_firstfunct(23,47))
print(my_firstfunct(1,2))
print(my_firstfunct(3,55))
print(my_firstfunct(4,89))
print(my_firstfunct(1,18))'''

# ACTIVITY 2
'''def Half(number):
    half_value = number/2
    return half_value

result = Half(28)
print(result)'''

# ACTIVITY 4
'''def list1(x,y):
    return x,y

b = [1,2,3]
#b = 64
d = 49
print(b,d)'''

# ACTIVITY 5


# ----------------------------------------- GROUP WORK ---------------------------------------------

# EXERCISE 4
'''print("\n--------- KINDERGARTEN CALCULATOR----------")
print("[A] Addition" '\n' "[B] Subtraction" '\n' "[C] Multiplication" '\n' "[D] Division")
print()

def input_retriever(select, num1, num2):
    if select == 'A':
        add = num1 + num2
        print("The total of the two numbers is ", add)
    elif select == 'B':
        subtract = num1 - num2
        print("The difference between the two numbers is ", subtract)
    elif select == 'C':
        multiply = num1 * num2
        print("The result of multiplication is ", multiply)
    elif select == 'D':
        division = num1 / num2
        print("The result of division is ", division)
    else:
        print("Invalid input")

input_retriever(select = input("Enter selection (in capital): "), num1=int(input("Enter first number : ")), num2=int(input("Enter second number : ")))'''

# EXERCISE 5
listNum = [123, 34, 56, 67, 90, 45]

def addNum(addition,y):
    addition.append(y)
    return addition

def  findFirst(theList):
    return theList[0]

def findMiddle(theList):
    middle = float(len(theList)) / 2
    if middle % 2 != 0:
        return theList[int(middle - .5)]
    else:
        return (theList[int(middle)], theList[int(middle - 1)])

def findLast(theList):
    return theList[-1]

def calcAverage(theList):
    avg = sum(theList)/(len(listNum))
    return avg

def findSmallest(theList):
    theList.sort()
    return theList[0]

def findLargest(theList):
    theList.sort()
    return theList[-1]

# calling addNum and letting the user input the additional value
y = int(input("Enter a number to be added into listNum : "))
print(addNum(listNum,y))

# calling function findFirst
print("The first number in the list is",findFirst(listNum))

# calling function findMiddle
print("The middle number in the list is",findMiddle(listNum))

# calling function findLast
print("The last number in the list is",findLast(listNum))

# calling function calAverage
print("The average for all the numbers in the list is",calcAverage(listNum))

# calling function findSmallest
print("The smallest number in the list is",findSmallest(listNum))

# calling findLargest
print("The largest number in the list is",findLargest(listNum))

























