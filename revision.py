# MODULE EXERCISE 1
# input: month, ans, leap
# output: days


'''ans = input("Press 'y' to quit, if not just press any other letter : ")

while (ans != 'y'):

    month = str.upper(input("Month (in capital letters): "))

    if (month == "JAN") or (month == "MAR") or (month == "MAY") or (month == "JUL") or (month == "AUG") or (month == "OCT") or (month == "DEC"):
        days = 31
    elif (month == "APR") or (month == "JUN") or (month == "SEP") or (month == "NOV"):
        days = 30
    elif (month == "FEB"):
        leap = input("is it a leap year? if yes press 'p' ")
        if leap == 'p':
            days = 29
        else:
            days = 28
    else:
        print("Invalid input entered! please try again")

    print("Month %s has %d days" %(month, days))
    ans = input("Press 'y' to quit : ")'''

# MODULE EXERCISE 2

'''num = int(input("Number 1 : "))
largest, smallest = num, num
sum = num
count = 1
ans = 'x'

while (ans != 'n'):
    num = int(input('number %d : '%(count + 1)))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    sum = sum + num
    count += 1
    ans = input("press 'n' to stop : ")

print("largest number of %d numbers : %d"%(count,largest))
print("smallest number of %d numbers : %d"%(count,smallest))
print("sum of %d numbers : %d "%(count,sum))'''

# MODULE EXERCISE 4
# input: total people, name, age
# output: totalNumber, totalKid, totalKid

'''print(" *Welcome to Residence Survey System* ")

totalNum, totalElder, totalKid = 0, 0, 0
house = 1

while house <= 3:
    count = 0
    people = int(input("Total people in house %d" %(house)))
    totalNum += people
    while people != 0:
        count += 1
        name = input("name %d : " %(count))
        age = int(input("age %d : " %(count)))

        if age > 60:
            totalElder += 1
        if age < 13:
            totalKid += 1
        people = people - 1
    house = house + 1

print("Total people : %d" %(totalNum))
print("Total elder(s) : %d" %(totalElder))
print("Total kid(s) : %d" %(totalKid))'''

# WEEK 9 LECTURE 2
sum = 0
avg = 0
list = []

# Ask user to input 3 values
for i in range(3):
    value = eval(input(" enter number %d : " %i))
    list.append(value)
    sum += value
print()

# Process
avg = sum/3

# Output
for i in range(3):
    print(" Value %d : " %i,list[i])

print("Average of the 3 numbers is", avg)
