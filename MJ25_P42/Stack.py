global Stack
global TopOfStack
Stack = ["-1" for i in range(0,20)] 
TopOfStack = -1

def Push(ItemToStore):
    global Stack
    global TopOfStack
    if TopOfStack == len(Stack)-1:
        return -1
    if TopOfStack == -1:
        TopOfStack = 0
        Stack[TopOfStack] = ItemToStore
        return 1

    TopOfStack += 1
    Stack[TopOfStack] = ItemToStore
    return 1


def Pop():
    global Stack
    global TopOfStack
    if TopOfStack == -1:
        return -1
    RemovedItem = Stack[TopOfStack]
    TopOfStack -= 1
    return RemovedItem

def ReadData(filename):
    global Stack
    global TopOfStack
    try:
        file = open(filename, "r")
        dataFetched = file.readline().strip()
        while dataFetched != "":
            PushReturn = Push(dataFetched)
            if PushReturn == -1:
                print("Stack full")
            dataFetched = file.readline().strip()
    except FileNotFoundError:
        print("File not found")

def Calculate():
    global Stack
    global TopOfStack
    Total = int(Pop())
    SignRead = Pop()
    ValueRead = int(Pop())
    while SignRead != -1 and ValueRead != -1:
        if SignRead == "+":
            Total += ValueRead
        elif SignRead == "-":
            Total -= ValueRead
        elif SignRead == "*":
            Total *= ValueRead
        elif SignRead == "/":
            Total /= ValueRead
        elif SignRead == "^":
            Total **= ValueRead
        SignRead = Pop()
        ValueRead = int(Pop())
        
    return Total

ReadData(input("Enter file name: "))
Total = Calculate()
print(f"Final total is: {Total}")


