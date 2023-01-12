# ACTIVITY 1, Q1
'''sum = 0
countEmp = 0
while countEmp < 3:
    hour= int(input('Please Enter Hours of Working'))
    rate= float(input('Please Enter Rate for each Hours'))
    payment = hour * rate
    print('Weekly payment is RM', payment)
    countEmp = countEmp + 1
    sum = sum + payment

print('All employees salary are processed.')
print('Total payment for %d employees is %.2f '%(countEmp,sum))'''
# A SUCCESS!!!

# ACTIVITY 1, Q3
'''X = 3
Count = 0
while Count < 3:
   X = X * X
   print(X)
   Count = Count + 1
print(Count)'''

# ACTIVITY 2, Qb
'''A,Z = 2,8
for NextCh in range (A,Z,4):
   print(NextCh)
   print( )'''

# Activity 2, Qc
'''import math
MAX = 4
print("\t",'i',"\t\t",'i * i',"\t\t",'Square root')
for i in range (1, MAX):
 Square = i*i
 Root_i = math.sqrt(i)
 print('{:>6}{:>12}{:>12.2f}'.format(i,Square,Root_i))'''

# EXERCISE 3
'''print("\t *Welcome to Mesra Stationary Shop* ")
print("\t\t List of things available ")
print("\t",'No',"\t\t",'Name',"\t\t",'Price(RM)')
print("\t",'1',"\t\t",'A4 Notebook',"\t\t",'3.50')
print("\t",'2',"\t\t",'Ball Pen',"\t\t\t",'1.20')
print("\t",'3',"\t\t",'Highlighter',"\t\t",'2.50')
print("\t",'4',"\t\t",'Calculator',"\t\t",'70.35')
print("\n")

totalPrice = 0
stop = ''

while (stop != 'x'):
    no = int(input("Choose number to pick [1-4] : "))
    if (no > 0) and (no < 5):

        if no == 1:
            item = 'A4 notebook'
            price = 3.50
        elif no == 2:
            item = 'ball pen'
            price = 1.20
        elif no == 3:
            item = 'highlighter'
            price = 2.50
        else:
            item = 'calculator'
            price = 70.35
        quantity = int(input("quantity of %s : " %item))
        totalPrice = totalPrice + (price * quantity)
        print("price of %s : RM %.2f" %(item,(price * quantity)))
        stop = str(input("press 'x' to proceed to payment"))

    else:
        exit("invalid input!")
        
print("Total payment : RM %.2f " %totalPrice)
paid = float(input("Amount paid : "))
print("Balance payment : RM %.2f" %(paid - totalPrice))
print("Thank you have a nice day!")'''
# A SUCCESS!!













