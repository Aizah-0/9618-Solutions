class NewRecord():
    #Key:Integer
    #Item1:Integer
    #Item2:Integer
    def __init__(self, Keyp, Item1P, Item2P):
        self.__Key = Keyp
        self.__Item1 = Item1P
        self.__Item2 = Item2P
    def GetKey(self):
        return self.__Key
    def GetItem1(self):
        return self.__Item1
    def GetItem2(self):
        return self.__Item2

global HashTable
global Spare
HashTable = []
Spare = []

def Initialise():
    global HashTable
    global Spare
    for i in range(0,200):
        HashTable.append(NewRecord(-1,-1,-1))
    for i in range(0,100):
        Spare.append(NewRecord(-1,-1,-1))

def CalculateHash(Key):
    global HashTable
    global Spare        
    HashValue = Key % 200
    return HashValue

def InsertIntoHash(RecordToStore):
    global HashTable
    global Spare 
    KeyValue = RecordToStore.GetKey()
    IndexValue = CalculateHash(KeyValue)
    if HashTable[IndexValue].GetKey() == -1:
        HashTable[IndexValue] = RecordToStore
    else:
        stored = False
        for i in range(0, 100):
            if Spare[i].GetKey() == -1:
                Spare[i] = RecordToStore
                break

def CreateHashTable():
    global HashTable
    global Spare
    try:
        filename = "HashData.txt"
        file = open(filename, "r")
        dataFetched = file.readline().strip()
        while dataFetched != "":
            Key, Item1, Item2 = dataFetched.split(",")
            RecordToStore = NewRecord(int(Key),int(Item1),int(Item2))
            InsertIntoHash(RecordToStore)
            dataFetched = file.readline().strip()
    except FileNotFoundError:
        print("File not found")

def PrintSpare():
    global HashTable
    global Spare
    for record in Spare:
        if record.GetKey() != -1:
            print(record.GetKey())

Initialise()
CreateHashTable()
PrintSpare()
