# declaring variables
stud_list = []
stop = 1

i = int(input("How many students records need to be processed? "))

for i in range(0,i):
    num_stud = int(input("Enter student ID : "))
    stud_list.append(num_stud)
print()

# ---------------- FUNCTION DEFINITIONS ---------------------------

# a function to add more student ID into the list
def addID(addition,y):
    addition.append(y)
    return addition

# a function to determine the early students
def early_stud(theList):
    half_list = theList[:len(theList)//2]
    return half_list

# a function to determine the late students
def late_stud(theList):
    half_list2 = theList[len(theList)//2:]
    return half_list2

# a function to determine the very very late student
def vv_late(theList):
    return theList[-1]

# ------------------- FUNCTION CALLERS----------------------------

# calling a function to add more student ID into the list
y = int(input("Additional ID to be added into the students list : "))
(addID(stud_list,y))

# calling the function to determine the early students
(early_stud(stud_list))

# calling the function to determine the late students
(late_stud(stud_list))

# calling the function to determine the very very late student
(vv_late(stud_list))

while stop != 'x':
    print("\n--------- STUDENT RECORDS ----------")
    print("[A] View List" '\n' "[B] Early Students" '\n' "[C] Late Students" '\n' "[D] Very Late Students")
    print()

    def input_retriever(select):
        if select == 'A':
            print("Students who came today : ",stud_list)
        elif select == 'B':
            print("Early students : ", early_stud(stud_list))
        elif select == 'C':
            print("The late students are : ", late_stud(stud_list))
        elif select == 'D':
            print("Very late student : ", vv_late(stud_list))
        else:
            print("Invalid input")

    input_retriever(select=input("Enter selection (in capital): "))
    stop = input("press 'y' to continue, press 'x' to quit) : ")

