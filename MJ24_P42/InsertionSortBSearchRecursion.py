NumberArray = [100,85,644,22,15,8,1]

def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else: 
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    IntegerArray[CheckItem+1] = LastItem
    return IntegerArray

ReturnedArray = RecursiveInsertion(NumberArray, len(NumberArray))
print("Recursive")
print(ReturnedArray)

def InterativeInsertion(IntegerArray):
    for i in range(0, len(IntegerArray) - 1):
        ValueToStore = IntegerArray[i]
        while ValueToStore > IntegerArray[i+1] and i >= 0:
            IntegerArray[i], IntegerArray[i+1] = IntegerArray[i+1], IntegerArray[i]
            i -= 1
    return IntegerArray

IntReturnedArray = InterativeInsertion(NumberArray)
print("Insertion")
print(IntReturnedArray)

def BinarySearch(IntegerArray, First, Last, ToFind):
    while Last >= First:
        MidPointer = int((First + Last)/2)
        if IntegerArray[MidPointer] == ToFind:
            return MidPointer   
        if ToFind > IntegerArray[MidPointer]:
            return BinarySearch(IntegerArray,MidPointer+1, Last,ToFind)
        if ToFind < IntegerArray[MidPointer]:
            return BinarySearch(IntegerArray, First, MidPointer - 1, ToFind)
    return -1

ToFind = 644
SearchReturn = BinarySearch(IntReturnedArray, 0, len(IntReturnedArray)- 1, ToFind)
if SearchReturn == -1:
    print(f"Not found")
else:
    print(f"{ToFind} found at index {SearchReturn}")


