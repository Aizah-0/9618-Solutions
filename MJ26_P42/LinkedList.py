LinkedList = [[9512,5], [5541,3], [1999,0], [6651,-1],[-1,6],[5612,1],[-1,-1],[-1,4]]
StartLinkedList = 2
StartEmptyList = 7

def PrintListItems(StartLinkedList, LinkedList):
    CurrentPointer = StartLinkedList
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = int(LinkedList[CurrentPointer][1])

def PrintEmptyList(StartEmptyList, LinkedList):
        CurrentPointer = StartEmptyList
        while CurrentPointer != -1:
            print(CurrentPointer)
            CurrentPointer = int(LinkedList[CurrentPointer][1])

print("Linked List")
PrintListItems(StartLinkedList, LinkedList)
print("Empty List")
PrintEmptyList(StartEmptyList, LinkedList)

def AddItem(DataToAdd, StartEmptyList, LinkedList):
    if LinkedList[StartEmptyList][0] != -1:
        print("List is full")
    else:
        LinkedList[StartEmptyList][0] = DataToAdd
        for i in range(0,len(LinkedList)):
            if LinkedList[i][1] == -1:
                 LinkedList[i][1] = StartEmptyList        
        StartEmptyList = int(LinkedList[StartEmptyList][1])
    return StartEmptyList

     
StartEmptyList = AddItem(8451, StartEmptyList, LinkedList)
print("List After Insertion")
PrintListItems(StartLinkedList, LinkedList)
print("Empty List After Insertion")
PrintEmptyList(StartEmptyList, LinkedList)

