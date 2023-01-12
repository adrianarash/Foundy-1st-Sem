# These are the counter for each grade
count_A = 0; count_B = 0; count_C = 0; count_D = 0; count_E = 0; count_F = 0


i = int(input("How many students records need to be processed? ")) # i ni is number of students specified

for i in range(0,i):
    name = input("Enter your name : ")
    ID = int(input("Enter your student ID : "))
    tutormark = int(input("Enter your tutorial test mark (/20) : "))
    testmark = int(input("Enter your test mark (/30) : "))

    if testmark + tutormark >= 40:
        EA = int(input('Enter student extended assignment mark (/50) : '))
        final_score = testmark + tutormark + EA
    else:
        final_score = testmark + tutormark

    # assigning grades
    if 80 <= final_score <= 100:
        grade = 'A'
        print('Student have obtained Grade',grade)
        count_A += 1
    elif 70 <= final_score < 80:
        grade = 'B'
        count_B += 1
        print('Student have obtained Grade',grade)
    elif 60 <= final_score < 70:
        grade = 'C'
        count_C += 1
        print('You have obtained Grade',grade)
    elif 50 <= final_score < 60:
        grade = 'D'
        count_D += 1
        print('Student have obtained Grade', grade)
    elif 40 <= final_score < 50:
        grade = 'E'
        count_E += 1
        print('Student have obtained Grade',grade)
    else:
        grade = 'F'
        count_F += 1
        print ('Student have obtained Grade',grade)

print('\n total students who got what grade')
print("%d students received grade A" %count_A)
print("%d students received grade B" %count_B)
print("%d students received grade C" %count_C)
print("%d students received grade D" %count_D)
print("%d students received grade E" %count_E)
print("%d students received grade F" %count_F)

if count_F > count_C + count_D + count_E:
    print("\n Analyse the assessment questions")
else:
    print("\n so far so good")

# calculating percentage using formula
i_percent_A = ((count_A / i)*100)
i_percent_B = ((count_B / i)*100)
i_percent_C = ((count_C / i)*100)
i_percent_D = ((count_D / i)*100)
i_percent_E = ((count_E / i)*100)
i_percent_F = ((count_F / i)*100)

# displaying percentage with these formulas
print("\n percentage of students who get what grade ")
print('A grade:', i_percent_A, '%')
print('B grade:', i_percent_B, '%')
print('C grade:', i_percent_C, '%')
print('D grade:', i_percent_D, '%')
print('E grade:', i_percent_E, '%')
print('F grade:', i_percent_F, '%')

if i_percent_A > 30:
    print("\n Class performance is Good")
elif i_percent_E or i_percent_F > 30:
    print("\n Class performance is bad")
















