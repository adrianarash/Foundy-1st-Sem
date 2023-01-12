# declaring variables
'''import random
listID = []
listgrade = []
listchoice=['A','B','C']
listIDjan21=[21345,21346,21347]
studentID=12345
option=1'''

# repititively process listID
'''while option != 0:
    studentID += 1
    listID.append(studentID)
    listgrade.append(random.choice(listchoice))
    option=int(input('do you wish to quit or continue with next student?press 0 to quit'))
print(listID)
print(listgrade)
clear=input('do you wish to clear the record of ID?')

if clear=='y':
    listIDcopy=listID.copy()
    listID.clear()
    print('no more record exist')
    print('list ID',listID)
    print('backup of list ID',listIDcopy)
    print('there are', listgrade.count('A'), 'student with A in the backuplist')
else:
    listID.extend(listIDjan21) #ni nanti listIDjan21 tu will be added into the list yang dah ada from atas
    print('after extension', listID)
    listID.insert(5,22222) #putting ID 22222 in index 5
    print('after insert', listID)
    print('is 22222 one of the ID?',22222 in listID)
    print('the index for 22222 is',listID.index(22222))
    value1 = int(input('which value to be remove , specify its index?'))
    listID.pop(value1)  # by position/index
    print(listID)
    value2 = int(input('which value to be remove ?'))
    print(listID)
    listID.remove(value2)  # by value
    print(listID)
    listID.reverse() # terbalikkan the order
    print(listID)'''

# LAB 1 - ACTIVITY 1
'''testList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
nameList= ['Lazarus','Luther','Orpheus','Raul','Rodolfo','Serafino','Silas','Vladamir']

print(nameList)
print (nameList.index('Orpheus'))
nameList.remove('Silas')
nameList.pop(5)
print(nameList)'''

# slicing dia lebih kurang macam for loop yang range tu, ada starting value, final value and increment value
'''s1 = slice(3)
s2 = slice(1, 5, 2)
print("\nList slicing")
print(testList[s1])
print(testList[s2])

print ("Initial values ", testList)
length=len(testList)
chunkSize=int(length/3)
start=0
end= chunkSize
for i in range(1, 4, 1):
    indexes=slice(start,end,1)
    listChunk=testList [indexes]
    print("Chunk",i,listChunk)
    listChunk.reverse()
    print('After reversing it',listChunk)
    start=end

    if (i != 2):
        end +=chunkSize
    else:
        end += length – chunkSize'''

# ACTIVITY 2
'''listFoo = [3,6,9,12,15,18,21]
listFaa = [4,8,12,16,20,24,28]

# Qa:
listFum = listFoo[4:7], listFaa[3:7]
print("listFum: ", listFum)

# Qb:
s1 = slice(1, 7, 2)
s2 = slice(0, 8, 2)

listFee = listFoo[s1], listFaa[s2]
print("ListFee: ", listFee)

# Qc:
listFoo.pop(4)
print("ListFoo after element 4 being removed: ", listFoo)
listFaa.insert(0,15)
print("ListFaa after element from listFoo is added: ", listFaa)

# Qd:
max_value = max(listFaa)
missingvalue = []

for i in range(1,max_value,1):
    if i not in listFaa:
        missingvalue.append(i)
print("missing values in listFaa are ", missingvalue)'''


# ACTIVITY 3
# Q1
listNum = list(range(1,201))
print("List of 200 numbers: ", listNum)

s1 = slice(0,100)
listOne = (listNum[s1])
print("List of numbers from 1- 100: ", listOne)

s2 = slice(100,201)
listTwo = (listNum[s2])
print("List of numbers from 101-200: ", listTwo)

# Q2
listNum = []
listDivTwo = []
listDivSeven = []
listDivTen = []

for i in range(1, 301):
    listNum.append(i)

    if i % 2 == 0:
        listDivTwo.append(i)

    if i % 7 == 0:
        listDivSeven.append(i)

    if i % 10 == 0:
        listDivTen.append(i)

print()
print("List of numbers divisable by 2: ", listDivTwo)
print("List of numbers divisable by 7: ", listDivSeven)
print("List of numbers divisable by 10: ", listDivTen)













