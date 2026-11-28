
global StackVowel
global StackConsonant
StackVowel = ["" for i in range(100)] #Stores vowels upto one hundred with first index 0
StackConsonant = ["" for i in range(100)] #Stores vowels upto one hundred with first index 0

global VowelTop
global ConsonantTop
VowelTop = 0 #stores index of next free space
ConsonantTop = 0 #stores index of next free space

def PushData(Letter):
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop
    vowels = ["a","e","i","o","u"]
    if Letter in vowels:
        if 0 <= VowelTop <= 100:
            StackVowel[VowelTop] = Letter
            VowelTop += 1
        else:
            print("Stack is full, letter not inserted")
    else:
        if 0 <= ConsonantTop <= 100:
            StackConsonant[ConsonantTop] = Letter
            ConsonantTop += 1
        else:
            print("Stack is full, letter not inserted")

def ReadData():
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop
    try:
        filename = "StackData.txt"
        file = open(filename, "r")
        DataFetched = file.readline().strip().lower()
        while DataFetched != "":
            PushData(DataFetched)
            DataFetched = file.readline().strip().lower()
    except FileNotFoundError:
        print("File not found")

def PopVowel():
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop
    if VowelTop == 0:
        return "No data"
    RemovedValue = StackVowel[VowelTop-1]
    StackVowel[VowelTop-1] = ""
    VowelTop -= 1
    return RemovedValue

def PopConsonant():
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop
    if ConsonantTop == 0:
        return "No data"
    RemovedValue = StackConsonant[ConsonantTop-1]
    StackConsonant[ConsonantTop-1] = ""
    ConsonantTop -= 1
    return RemovedValue

ReadData()
JoinedReturn = ""
for i in range(5):
    UserChoice = input("Vowel or Consonant? ").lower()
    if UserChoice == "vowel":
        ReturnedVal = PopVowel()
    elif UserChoice == "consonant":
        ReturnedVal = PopConsonant()
    JoinedReturn += ReturnedVal
print(JoinedReturn)
