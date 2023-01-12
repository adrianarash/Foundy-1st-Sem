stop = 1
while stop != 'x':
    print("\n----------------select--------------------")
    print("[A] One" '\n' "[B] Two" '\n' "[C] Save")

    def Num_Tri_One():
        file = open ("tri_one.txt","w")
        for i in range(1,6):
            for j in range(1, i+1):
                print(j, end = '0')
                x = str(i)
                file.write(x)
                file.write('0')
                i +=1
            print()
            file.write('\n')

        print("file successfully generated")
        file.close()

    def Num_Tri_Two():
        file = open ("tri_two.txt","w")
        for i in range(1,6):
            for j in range(1, i+1):
                print(i, end = '0')
                x = str(i)
                file.write(x)
                file.write('0')
                i += 1
            print()
            file.write('\n')
        print("file successfully generated")
        file.close()

    def Save_Triangle():
        t1 = open('tri_one.txt')
        t2 = open('tri_two.txt')
        t3 = open('triangle.txt', 'a')
        for x in t1.readlines():
            t3.write(x)
        for x in t2.readlines():
            t3.write(x)
        t1.close()
        t2.close()
        t3.close()

    def input_retriever(select):
        if select == 'A':
            print("\nFile 1 : ",Num_Tri_One())
        elif select == 'B':
            print("\nFile 2 : ", Num_Tri_Two())
        elif select == 'C':
            Save_Triangle()
            print("File saved successfully")
        else:
            print("Invalid input")

    input_retriever(select=input("Enter selection (in capital): "))

    stop = input("Press 'y' to continue, press 'x' to stop : ")



