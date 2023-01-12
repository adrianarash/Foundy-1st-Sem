# EA Jan2021, Question 1

# defining a function to calculate earnings
def calculateEarnings(initialMoney, interestRate):
    # these two variables are used to display the year when the initial amount will be doubled
    doubleValue = 0
    starter = 1
    # set the initial amount to another variable
    # because after the year, the initialMoney value for calculation will differ
    initialMoneyAfterYear = initialMoney

    # loop is used for each year calculation
    for i in range(1, 31):
        totalMoney = initialMoneyAfterYear * (1 + (interestRate/100))**(i)

        if (i==1):
            print("After",i,"year : RM %.2f"%(totalMoney))
        if (i==10):
            print("After", i, "years : RM %.2f"%(totalMoney))
        if (i==20):
            print("After", i, "years : RM %.2f"%(totalMoney))
        if (i==30):
            print("After", i, "years : RM %.2f"%(totalMoney))

        # this is used to display the year when initial money is doubled
        if totalMoney >= (2* initialMoney):
            if starter == 1:
                doubleValue = i
                starter += 1

        # after year the total money will be initial money for next year
        initialMoneyAfterYear = totalMoney

    print("\n**************************************************************")
    print("it will take about",doubleValue,"years for your investment to double up")

print("\t\t\t\tWELCOME TO PRO INVESTMENT")

# prompt input from user
initialMoney = float(input("\nHow much money do you want to invest? : "))
interestRate = float(input("Yearly interest rate (%) : "))

print("\n====================================================================")
print("\t\t\t\t\t\tINVESTMENT")
print("====================================================================")

# calling function
calculateEarnings(initialMoney,interestRate)









