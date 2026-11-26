#main program

#1D Array with nine items
TheData = ["laptop","tablet", "printer","computer", "processor", "monitor", "memory", "cable", "touchscreen"] 

def FindLongestShortest(ArrayOfStrings):
    longest = 1
    shortest = 20

    for i in range(0,len(ArrayOfStrings)):
        if len(ArrayOfStrings[i]) > longest:
            longest = len(ArrayOfStrings[i])
            longest_word = ArrayOfStrings[i]

        if len(ArrayOfStrings[i]) < shortest:
                shortest = len(ArrayOfStrings[i])
                shortest_word = ArrayOfStrings[i]

    print(f"Longest word: {longest_word} Shortest word: {shortest_word}")  

def InsertionSort(ArrayOfStrings):
    for i in range(1, len(ArrayOfStrings)):
         Value_to_sort = ArrayOfStrings[i]
         while ArrayOfStrings[i - 1] > Value_to_sort and i > 0: 
              ArrayOfStrings[i], ArrayOfStrings[i-1] = ArrayOfStrings[i-1], ArrayOfStrings[i]
              i-=1
    return ArrayOfStrings

print("Before sorting")
FindLongestShortest(TheData)
TheData = InsertionSort(TheData)
print("After sorting")
print(TheData)

