# Activity 4

yes_ans = 0 #initialize value
min_on_net = int(input("how many hours do you spend a day on the Net"))

#Converting the unit
hours_on_net = min_on_net/60

if hours_on_net >= 2:
    print("You might be addicted to the Net")

    ans1 = str.lower(input("Do you stay online longer than you intended?"))
    if ans1 == 'yes':
        yes_ans +=1
    ans2 = str.lower(input("Do you hear other people in your life complain about how much time you spend online?"))
    if ans2 == 'yes':
        yes_ans +=1
    ans3 = str.lower(input("Do you say or think, “Just a few more minutes” when online?"))
    if ans3 == 'yes':
        yes_ans +=1
    ans4 = str.lower(input("Do you try and fail to cut down on how much time you spend online?"))
    if ans4 == 'yes':
        yes_ans +=1
    ans5 = str.lower(input("Do you hide how long you’ve been online?"))
    if ans5 == 'yes':
        yes_ans +=1

    if yes_ans >= 3:
        print("you are an INTERNET ADDICT")
    else:
        print("control your internet usage")

else:
    print("keep up the good habit baby")







