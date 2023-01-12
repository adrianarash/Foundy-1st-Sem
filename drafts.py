import pandas as pd

# This is my function to record data into text file 1
def EnterDataSensor1():
    file1="dataSensor1.txt"
    quit = ""
    outfile=open(file1,"w")
    outfile.write("SensorID,City,PressureReading ")

    while quit != 0:
        sensorID, city, pressureReading = input("Enter Sensor ID, City, Pressure Reading :").split()
        outfile.write("\n")
        outfile.write(sensorID+",")
        outfile.write(city+",")
        outfile.write(pressureReading)
        quit = int(input("Press 1 to continue and 0 to exit:"))
    outfile.close()

# This is my function to record data into text file 2
def EnterDataSensor2():
    file2="dataSensor2.txt"
    quit = ""
    outfile1 = open(file2,"w")
    outfile1.write("SensorID,City,PressureReading ")

    while quit != 0:
        sensorID, city, pressureReading = input("Enter Sensor ID, City, Pressure Reading (2nd File) :").split()
        outfile1.write("\n")
        outfile1.write(sensorID+",")
        outfile1.write(city+",")
        outfile1.write(pressureReading)
        quit = int(input("Press 1 to continue and 0 to exit:"))
    outfile1.close()

# This function is to convert textfiles to pandas
def ConvertToPanda():
    df1 = pd.read_csv('dataSensor1.txt', sep=",")
    df2 = pd.read_csv('dataSensor2.txt', sep=",")
    print(df1.to_string())
    print(df2.to_string())

# this is to combine the two tables/textfile made by panda data frame
def ConcateTextfiles():
    df1 = pd.read_csv('dataSensor1.txt', sep=",")
    df2 = pd.read_csv('dataSensor2.txt', sep=",")
    df3 = pd.concat([df1, df2], ignore_index=True, axis=0)
    print(df3)

# this function is to look at the highest and lowest pressure reading
def HighLowValue():
    df1 = pd.read_csv('dataSensor1.txt', sep=",")
    df2 = pd.read_csv('dataSensor2.txt', sep=",")
    df3 = pd.concat([df1, df2], ignore_index=True, axis=0)
    df["PressureReading"] = pd.to_numeric(df["PressureReading"], downcast="float")
    print("\nHighest profit pressure reading : %.3f" % (df3['PressureReading'].max()))
    print("Lowest price per unit : %.3f" % (df3['PressureReading'].min()))

def Average():
    ConcateTextfiles()
    df = pd.DataFrame({"PressureReading": ['360.5', '400.5', '678.7', '859.6', '567.7', '123.4', '975.7', '65.6']})
    df["PressureReading"] = pd.to_numeric(df["PressureReading"], downcast="float")
    average = df["PressureReading"].mean()
    print("\nAverage pressure reading : %.3f"%average,"psi" )


# ------------------------- MAIN PROGRAM -------------------------------------------
print("----- Adriana's Gas Corporation -----")
print("1. Record data in Data Sensor 1")
print("2. Record data in Data Sensor 2")
print("3. View data sensor 1 and data sensor 2")
print("4. View overall data ")
print("5. View highest and lowest pressure reading")
print("6. View average pressure reading")
print("7. Quit")

stop = 1
while stop != 0:
    select = int(input('\nEnter choice [1-7] : '))
    if (select == 1):
        EnterDataSensor1()
    elif (select == 2):
        EnterDataSensor2()
    elif (select == 3):
        ConvertToPanda()
    elif (select == 4):
        ConcateTextfiles()
    elif (select == 5):
        HighLowValue()
    elif (select == 6):
        Average()
    else:
        break
