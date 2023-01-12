# QUIZ 7
stop = 1

while stop != 'x':
    print("\n--------- Select operation----------")
    print("[A] Calculate Perimeter of Rectangle" '\n' "[B] Calculate Area of Triangle" '\n' "[C] Convert Celsius to Fahrenheit" '\n' "[D] Convert Fahrenheit to Celsius")
    select = input("\nEnter selection (in capital): ")
    print()

    if select == 'A':
        h1 = int(input("enter height: "))
        b1 = int(input("enter base: "))
        # defining function rectangle
        def rectangle(h1,b1):
            perimeter = (h1*2) + (b1*2) #formula for d calculation
            return perimeter # what am i suppose to return? the damn variable lahh

        # calling function rectangle
        rectangle(h1,b1)
        total_perimeter = rectangle(h1,b1) # ni i simpan the calculation yang function tu dah calculatekan for me in a variable called total perimeter
        print("The perimeter for the rectangle is ", total_perimeter)
        stop = input("Do you wish to quit? press x :")

    elif select == 'B':
        h2 = int(input("enter height: "))
        b2 = int(input("enter base: "))

        # defining function triangle
        def triangle(h2,b2):
            area = (h2*b2)/2
            return area

        # calling function triangle and minta user enter value yang diorang nak
        triangle(h2,b2)
        total_area = triangle(h2,b2)
        print("The area for the triangle is ",total_area)
        stop = input("Do you wish to quit? press x :")

    elif select == 'C':
        temp_C = eval(input("Enter temperature in degree celsius: ")) # i baru tahu that i can ask for input separately here
        # defining function conv_C
        def conv_C(temp_C):
            temp_F = temp_C * 1.8 + 32
            return temp_F

        # calling function conv_C
        conv_C(temp_C) # thissss wajib
        converted_C = conv_C(temp_C) # i simpan value yang the function dah execute tu dalam variable converted_C
        print("The temperature in Fahrenheit is", converted_C)
        stop = input("Do you wish to quit? press x :")

    elif select == 'D':
        temp_F2 = eval(input("Enter temperature in Fahrenheit: "))

        def conv_F(temp_F2):
            temp_C2 = (temp_F2 - 32)/ 1.8
            return temp_C2

        # this is how you call the function, you basically just tulis balik nama function tu lmao
        conv_F(temp_F2)  # wait i just found out takyah pun takpe whattttt
        converted_F = conv_F(temp_F2)
        print("The temperature in Celsius is", converted_F)
        stop = input("Do you wish to quit? press x :")

    else:
        print("invalid selection. Please try again.")










