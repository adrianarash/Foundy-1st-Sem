# QUESTION 1
listID = []
listlocation = []
listamount = []
count = 1
response = 'y'

while response != 'x':

    print("\n--------- MIJA Oil Monitoring System ----------")
    print("[A] Record location details" '\n' "[B] View records" '\n' "[C] Update " '\n' "[D] Delete record" '\n' "[E] Production details" )
    print()

    select = input("Enter selection : ")

    if select == 'A':
        i = int(input("How many locations do you want to record? : "))
        for i in range(0,i):
            location_ID = (int(input("Enter location ID : ")))
            listID.append(location_ID)
            location = input("Enter location : ")
            listlocation.append(location)
            oil_amount = input("Enter amount of oil produced (thousand barrels per day) : ")
            listamount.append(oil_amount)
            count += 1

            #response = input("Press 'y' to continue, press 'x' to quit : ")
        print()

    #viewrecord
    elif select == 'B':
        for i in range(len(listID)):
            print("Location ID : ", listID[i])
            print("Location : ", listlocation[i])
            print("Amount of Oil Produced : ", listamount[i])
        print()

    #updatenewvalue
    elif select == 'C':
        print("Which location do you want to change?\n")
        location_ID = int(input("Enter location ID : "))
        listlocation.pop(listID.index(location_ID))  # removing the old location name
        location = input("New location name : ")
        listlocation.insert(listID.index(location_ID), location)  # inserting the new location name to the location list
        oil_amount = int(input("New oil amount : "))
        listamount.insert(listID.index(location_ID), oil_amount)  # inserting the new location name to the location list
        print("The location and oil amount has been updated successfully.\n")
        quit = input("Press 'y' to continue, press 'x' to stop : ")

    #delete record based on ID
    elif select == 'D':
        print("Which location record do you want to delete?\n")
        location_ID = int(input("Enter ID : "))
        listlocation.pop(listID.index(location_ID))
        listamount.pop(listID.index(location_ID))
        listID.remove(location_ID)
        print("The location record have been deleted successfully.\n")
        quit = input("Press 'y' to continue, press 'x' to stop : ")

    #compute sum and average

# QUESTION 3
'''year =
age =

if year > 2020 and year <= 2029:
    free vaccine
elif year >= 2030 and year < 2079:
    display status eligible or not
    if job == 'G'
        vaccine at discounted price
    else:
        display assistance
elif year > 2079:'''

df = pd.DataFrame({"PressureReading": ['360.5', '400.5', '678.7', '859.6', '567.7', '123.4', '975.7', '65.6']})
df4 = pd.DataFrame({"SensorID": ['101', '102', '103', '104', '501', '502', '503', '504']})
df5 = pd.DataFrame({"City": ['Ipoh', 'Malim', 'Klang', 'Tapah', 'Kerteh', 'Kuantan', 'Gambang', 'Gebeng']})

df = pd.DataFrame({"PressureReading": ['360.5', '400.5', '678.7', '859.6', '567.7', '123.4', '975.7', '65.6']})
'''df4 = pd.DataFrame({"SensorID": ['101', '102', '103', '104', '501', '502', '503', '504']})
df5 = pd.DataFrame({"City": ['Ipoh', 'Malim', 'Klang', 'Tapah', 'Kerteh', 'Kuantan', 'Gambang', 'Gebeng']})'''
max_value = df['PressureReading'].max()
min_value = df['PressureReading'].min()
print("\nHighest pressure reading : ", max_value)
print("Lowest pressure reading : ", min_value)
dataType = df.dtypes
print(dataType)

df4 = df3[df3["PressureReading"] == df3["PressureReading"].max()]
df4.loc[0]
print("\nThe highest pressure reading : ",highest)
df4 = df3[df3["PressureReading"] == df3["PressureReading"].min()]
df4.loc[1]
print("The lowest pressure reading : ",lowest)
