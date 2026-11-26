import random

Numbers = []
while len(Numbers) < 20:
    RandomNumber = random.randint(0,100)
    if RandomNumber not in Numbers:
        Numbers.append(RandomNumber)

def PrintArray(Numbers):
    line = ""
    for Item in Numbers:
        line = line + str(Item) + " "
    print(line)

def BubbleSort(Numbers):
    for o in range(0,len(Numbers)-1):
        swapped = False
        for i in range(0, len(Numbers) - 1 - o):
            if Numbers[i] > Numbers[i+1]:
                temp = Numbers[i+1]
                Numbers[i+1] = Numbers[i]
                Numbers[i] = temp
                swapped = True
        if not swapped:
            break

    return Numbers

PrintArray(Numbers)
Numbers = BubbleSort(Numbers)
print("Sorted")
PrintArray(Numbers)

def RecursiveBinarySearch(Numbers, LB, UB, ValueToFind):
    while LB <= UB:
        MidPoint = int((LB + UB)/2)
        if ValueToFind == Numbers[MidPoint]:
            return MidPoint
        elif Numbers[MidPoint] < ValueToFind:
            return RecursiveBinarySearch(Numbers, MidPoint + 1, UB, ValueToFind)
        elif Numbers[MidPoint] > ValueToFind:
            return RecursiveBinarySearch(Numbers, LB, MidPoint - 1, ValueToFind)
    return -1


UserNumber = int(input("Enter an integer number: "))
SearchReturnValue = RecursiveBinarySearch(Numbers, 0, len(Numbers)-1, UserNumber)

if SearchReturnValue == -1:
    print("Not found")
else:
    print(f"Found at position {SearchReturnValue}")





