# ACTIVITY 1
stop = ''
select = ''

while (stop != 'Q'):

    print("Enter two numbers to begin calculations")
    num1 = int(input("Please enter the first number"))
    num2 = int(input("Please enter the second number"))
    print("\n")
    print("--------- Select operation----------")
    print("[A]dd" '\n' "[S]ubtract" '\n' "[M]ultiply" '\n' "[D]ivide" '\n' "[Q]uit")
    print()
    select = input("Enter choice of operation : ")
    select = select.upper()
    print("------Calculating-------")


    if select == 'A':
        print(num1,'+',num2,'=',(num1 + num2))
    elif select == 'S':
        print(num1, '-', num2, '=', (num1 - num2))
    elif select == 'M':
        print(num1, '*', num2, '=', (num1 * num2))
    elif select == 'D':
        while num2 == 0:
            num2 = int(input("Denominator cannot be 0, enter a valid denominator :"))
        print(num1, '/', num2, '=', (num1/num2))
    else:
        print("invalid choice")

    stop = input("press 'Q' to quit")







