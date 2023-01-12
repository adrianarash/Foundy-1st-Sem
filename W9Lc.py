# WEEK 9 LECTURE 2
option = 1; index = 0
listexam = []
studentID = []
numofsem = []


while option != 0:
    ID = int(input('Please enter student ID:'))
    studentID.append(ID)
    sem = int(input('Please enter the number of semesters you have attended:'))
    numofsem.append(sem)
    exam = int(input('Please enter programming exam score (/50):'))
    listexam.append(exam)

    if (exam <=50 and exam >=0):
        exampercent = exam * 2
        if 90 <= exampercent <= 100:
            print('You have obtained Grade A.')
        elif 80 <= exampercent <= 89:
            print('You have obtained Grade B.')
        elif 70 <= exampercent <= 79:
            print('You have obtained Grade C.')
        elif 60 <= exampercent <= 69:
            print('You have obtained Grade D.')
        else:
            print ('You have obtained Grade F.')
        print('Your student ID is',studentID[index],'your exam result is',listexam[index],'. your number of semester is',numofsem[index],'. Your programming exam score is',exampercent,'%.')

        if sem == 3:
            if 80 <= exampercent <= 100:
                print('Your self-improvement program will be Mighty Musang King.')
        if sem == 2:
            if 60 <= exampercent <= 79:
                print('Your self-improvement program will be Fighting Pomelo.')
        if sem == 0:
            if 0 <= exampercent <= 59:
                print('Your self-improvement program will be Mushy Banana.')
            else:
                print('There is no self-improvement program for you.')
    else:
        print('Invalid grade.')
    index += 1
    option = int(input('Please enter option:'))
print('the recorded student ID is', studentID)
print('the recorded exam result is', listexam)
print('the recorded semester is', numofsem)
