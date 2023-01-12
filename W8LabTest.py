# input : name, age, no_house
# process : check the age when they'll turn 60
# output : display the year the customer will turn 60
# statements : 1) if age = 60 within year 2020 and 2029, theyre eligibile to receive a free termite and cockroach control package.
# 2) if age = 60 within year 2030 and 2060, get a cockroach control package at a discounted price
# 3) if no_house > 5, get 50% discount
# 4) if no_house <= 5, they can enjoy a 10% discount
# 5) if age = 60 after year 2060, only be eligible for a free consultation
# nanti declare variables year juga

# declaring variables
current_year = 2021
year = 0

# prompt user to start
stop = input("Press 'x' to quit, if not just press any other letter : ")

# Statements and looping
while stop != 'x':

    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    no_house = int(input("Enter number of house(s) : "))
    #birth_year = int(input("Enter your birth year : "))


    #age = current_year - birth_year
    print("Customer is %d years old" % (age))

    if no_house > 5:
        print("enjoy a 50% discount")

        if (age == 60) and (year == 2020 - 2029):
                    print("eligibile to receive a free termite and cockroach control package")

        elif (age == 60) and (year == 2030 - 2060):
                print("eligible to receive cockroach control package at a discounted price")

        else:
            print("eligible for a free consultation only")

    else:
        print("enjoy a 10% discount")

    stop = input("press 'x' to exit")






