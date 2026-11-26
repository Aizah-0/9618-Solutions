global TreeArray
global RootPointer
global FreeNode

TreeArray = [[-1,-1,-1] for i in range(0,50)]
RootPointer = -1
FreeNode = 0

def AddNode(DataToAdd):
    global TreeArray
    global RootPointer
    global FreeNode
    if FreeNode <= len(TreeArray)-1:
        TreeArray[FreeNode][1] = DataToAdd

        if RootPointer == -1:
            RootPointer = FreeNode
        else:
            PointerUpdated = False
            CurrentPointer = RootPointer
            while not PointerUpdated:
                if DataToAdd > TreeArray[CurrentPointer][1]:
                    if TreeArray[CurrentPointer][2] == -1:
                        TreeArray[CurrentPointer][2] = FreeNode
                        PointerUpdated = True
                    else:
                        CurrentPointer = TreeArray[CurrentPointer][2]
                else:
                    if TreeArray[CurrentPointer][0] == -1:
                        TreeArray[CurrentPointer][0] = FreeNode
                        PointerUpdated = True
                    else:
                        CurrentPointer = TreeArray[CurrentPointer][0]
        FreeNode += 1
    else:
        print("The tree is full")

filename = "TreeData.txt"
try:
    file = open(filename, "r")
    dataFetched = file.readline().strip()
    while dataFetched != "":
        AddNode(int(dataFetched))
        dataFetched = file.readline().strip()
    file.close()
except FileNotFoundError:
    print("File not found")

def WriteAllToFile():
    filename = "Tree.txt"
    file = open(filename, "w")
    for line in TreeArray:
        file.write(f"{line[0]},{line[1]},{line[2]}\n")
    file.close

WriteAllToFile()
