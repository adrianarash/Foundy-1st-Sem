# Question 1
sum_A, sum_B, sum_C, sum_D, sum_E = 0,0,0,0,0
listTopSell = []
listLowSell = []
quit = 'y'

while quit != 'x':
    print("\n-------Snack2u---------")
    print("[A] Meal A (RM3.50)")
    print("[B] Meal B (RM5.50)")
    print("[C] Meal C (RM8.50)")
    print("[D] Meal D (RM6.50)")
    print("[E] Meal E (RM4.80)")

    select = input("\nWhich meal do you want to calculate? : ")

    if select == 'A':
        meal = 'Meal A'
        for i in range(1,6):
            meal_sold_A = int(input("Meal sold in day %d : "%i))
            sum_A += meal_sold_A
            profit_A = sum_A * 3.5
            print("Profit for meal A is : RM%.2f "%profit_A)
            total_profit = profit_A
        if total_profit >= 100:
            listTopSell.append(meal)
        elif total_profit <= 50:
            listLowSell.append(meal)
        quit = input("Press 'y' to continue, press 'x' to stop : ")

    elif select == 'B':
        meal = 'Meal B'
        for j in range(1,6):
            meal_sold_B = int(input("Meal sold in day %d : "%j))
            sum_B += meal_sold_B
            profit_B = sum_B * 5.5
            print("Profit for meal B is : RM%.2f "%profit_B)
            total_profit = profit_B
        if total_profit >= 100:
            listTopSell.append(meal)
        elif total_profit <= 50:
            listLowSell.append(meal)
        quit = input("Press 'y' to continue, press 'x' to stop : ")

    elif select == 'C':
        meal = 'Meal C'
        for k in range(1,6):
            meal_sold_C = int(input("Meal sold in day %d : " %k))
            sum_C += meal_sold_C
            profit_C = sum_C * 8.5
            print("Profit for meal C is : RM%.2f " % profit_C)
            total_profit = profit_C
        if total_profit >= 100:
            listTopSell.append(meal)
        elif total_profit <= 50:
            listLowSell.append(meal)
        quit = input("Press 'y' to continue, press 'x' to stop : ")

    elif select == 'D':
        meal = 'Meal D'
        for l in range(1,6):
            meal_sold_D = int(input("Meal sold in day %d : " %l))
            sum_D += meal_sold_D
            profit_D = sum_D* 6.5
            print("Profit for meal D is : RM%.2f " % profit_D)
            total_profit = profit_D
        if total_profit >= 100:
            listTopSell.append(meal)
        elif total_profit <= 50:
            listLowSell.append(meal)

        quit = input("Press 'y' to continue, press 'x' to stop : ")

    elif select == 'E':
        meal = 'Meal E'
        for m in range(1,6):
            meal_sold_E = int(input("Meal sold in day %d : " %m))
            sum_E += meal_sold_E
            profit_E = sum_E * 4.8
            print("Profit for meal E is : RM%.2f " % profit_E)
            total_profit = profit_E
        if total_profit >= 100:
            listTopSell.append(meal)
        elif total_profit <= 50:
            listLowSell.append(meal)
        quit = input("Press 'y' to continue, press 'x' to stop : ")

print("Top selling meals : ", listTopSell)
print("Low selling meals : ", listLowSell)





