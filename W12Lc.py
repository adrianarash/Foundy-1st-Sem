import pandas as pd


# to store the data from ipoh into textfile
def RecordDataOutlet1():
    file1 = "outlet1.txt"
    response = ""
    outfile = open(file1, "w")
    outfile.write("ItemID,Item,Price,NetProfit")

    while response != '0':
        ItemID, Item, Price, NProfit = input("Enter ItemID,Item Name,Price and its Net Profit in RM:").split()
        outfile.write("\n")
        outfile.write(ItemID + ",")
        outfile.write(Item + ",")
        outfile.write(Price + ",")
        outfile.write(NProfit)
        response = input("Press enter to continue and zero(0) to stop:")
    outfile.close()


# to store the data from sitiawan into textfile
def RecordDataOutlet2():
    file2 = "outlet2.txt"
    response = ""
    outfile1 = open(file2, "w")
    outfile1.write("ItemID,Item,Price,NetProfit")

    while response != '0':
        ItemID, Item, Price, NProfit = input("Enter ItemID,Item Name, Price and its Net Profit in RM:").split()
        outfile1.write("\n")
        outfile1.write(ItemID + ",")
        outfile1.write(Item + ",")
        outfile1.write(Price + ",")
        outfile1.write(NProfit)
        response = input("Press enter to continue and zero(0) to stop:")
    outfile1.close()


# to add new data into textfile
def AddDataOutlet():
    outlet = int(input("Outlet [1]/[2] : "))
    response = ""

    while outlet != 1 and outlet != 2:
        outlet = int(input("Outlet [1]/[2] : "))

    if outlet == 1:
        file1 = "outlet1.txt"
        outfile = open(file1, "a")
    else:
        file2 = "outlet2.txt"
        outfile = open(file2, "a")

    while response != '0':
        ItemID, Item, Price, NProfit = input("Enter ItemID,Item Name,Price and its Net Profit in RM:").split()
        outfile.write("\n")
        outfile.write(ItemID + ",")
        outfile.write(Item + ",")
        outfile.write(Price + ",")
        outfile.write(NProfit)
        response = input("Press enter to continue and zero(0) to stop:")
    outfile.close()


# to read and then combine the data from 2 textfiles by using panda
def RetrieveOutletRecord():
    df1 = pd.read_csv('outlet1.txt', sep=",")
    df2 = pd.read_csv('outlet2.txt', sep=",")
    print("\n\tOUTLET1 - IPOH")
    print(df1.to_string())
    print("\n\tOUTLET2 - SITIAWAN")
    print(df2.to_string())
    # concatrecord(df1,df2)#function call


def concatrecord():
    df1 = pd.read_csv('outlet1.txt', sep=",")
    df2 = pd.read_csv('outlet2.txt', sep=",")
    df3 = pd.concat([df1, df2], ignore_index=True, axis=0)
    print("\n\tALL OUTLETS")
    print(df3)
    print("\nHighest profit per month : RM %.2f" % (df3['NetProfit'].max()))
    print("Lowest price per unit : RM %.2f" % (df3['Price'].min()))
    # Filteritem(df3)


def Filteritem():
    df1 = pd.read_csv('outlet1.txt', sep=",")
    df2 = pd.read_csv('outlet2.txt', sep=",")
    df3 = pd.concat([df1, df2], ignore_index=True, axis=0)
    choice = input('\nPlease enter item to be searched')
    filterItem = df3[df3['Item'] == choice]
    print(filterItem)


# main program

option = 1
print("Type your choice")
print("1. Record data in Outlet 1")
print("2. Record data in Outlet 2")
print("3. Add data in Outlet 1/2")
print("4. Display both outlets")
print("5. Find the highest profit and lowest price")
print("6. Searching for item")
print("7. To stop")

while option != 0:
    n = int(input('\nEnter choice:'))
    if (n == 1):
        RecordDataOutlet1()
    elif (n == 2):
        RecordDataOutlet2()
    elif (n == 3):
        AddDataOutlet()
    elif (n == 4):
        RetrieveOutletRecord()
    elif (n == 5):
        concatrecord()
    elif (n == 6):
        Filteritem()
    else:
        break
