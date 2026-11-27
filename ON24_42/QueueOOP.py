class Queue():
    def __init__(self):
        self.QueueArray = [0] * 100
        self.HeadPointer = 0
        self.TailPointer = 0

TheQueue = Queue()
TheQueue.HeadPointer = -1
TheQueue.TailPointer = 0
TheQueue.QueueArray [-1] * 100

def Enqueue(AQueue, TheData):
    if AQueue.HeadPointer == -1:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.HeadPointer = 0
        AQueue.TailPointer += 1
        return 1, AQueue
    else:
        if AQueue.TailPointer > len(AQueue.QueueArray):
            return -1, AQueue
        else:
            AQueue.QueueArray[AQueue.TailPointer] = TheData
            AQueue.TailPointer += 1
            return 1, AQueue

def ReturnAllData(TheQueue):
    JoinedString = ""
    for i in range(TheQueue.HeadPointer,TheQueue.TailPointer):
        QueueItem = TheQueue.QueueArray[i]
        JoinedString += f"{QueueItem} "
    return JoinedString

print("Enter 10 numbers greater than or equal to zero: ")
for i in range(10):
    Num = int(input())
    while Num <= 0:
        print("Number has to be greater than zero: ")
        Num = int(input())
    Eunqueueflag, TheQueue = Enqueue(TheQueue, Num)
    if Eunqueueflag == -1:
        print("The Queue is full")
    else:
        print("Item added to queue")
print(ReturnAllData(TheQueue))

def Dequeue(TheQueue):
    if TheQueue.TailPointer == 0:
        return -1
    ValueRemoved = TheQueue.QueueArray[TheQueue.HeadPointer]
    TheQueue.HeadPointer += 1
    return ValueRemoved

for i in range(2):
    DequeueReturn = Dequeue(TheQueue)
    if DequeueReturn == -1:
        print("Queue Empty")
    else: 
        print(DequeueReturn)
print(ReturnAllData(TheQueue))
