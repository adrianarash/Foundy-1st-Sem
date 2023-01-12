# PROMPT INPUT FROM USER
student_ID = int(input("Student ID : "))
name = input("Name : ")
num_sem = int(input("Number of semester(s) : "))
exam_mark = int(input("Exam mark (/50) : "))

# CLASSIFYING GRADES AND WHICH PROGRAMME TO JOIN
if (exam_mark <=50 and exam_mark >=0):

    exam_score = int(exam_mark * 2)
    print("Exam mark : ", exam_score)

    if 90 <= exam_score <= 100:
        print('You have obtained Grade A.')
    elif 80 <= exam_score <= 89:
        print('You have obtained Grade B.')
    elif 70 <= exam_score <= 79:
        print('You have obtained Grade C.')
    elif 60 <= exam_score <= 69:
        print('You have obtained Grade D.')
    else:
        print ('You have obtained Grade F.')


    if (num_sem == 3) and (exam_score >= 80 and exam_score <= 100):
            print('Join the Mighty Musang King self-improvement programme.')
    elif (num_sem == 2) and (exam_score >= 60 and exam_score <= 79):
            print('Join the Fighting Pomelo self-improvement programme.')
    elif (num_sem == 1) and (exam_score <= 59):
            print('Join the Mushy Banana self-improvement programme.')
    else:
        print("No self improvement program for you.")

else:
    print("Exam mark is not eligible.")









