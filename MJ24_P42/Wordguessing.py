global WordArray
WordArray = []

def Play():
    global WordArray
    UserCorrect = 0
    print(f"Main word is {WordArray[0]}, Number of answers is {len(WordArray)-1}")
    print("Enter no to stop")
    UserAns = input("Your answer: ").lower()
    while UserAns != "no":
        if UserAns in WordArray and UserAns != WordArray[0]:
            print("Corrent answer")
            UserCorrect += 1
            for i in range(1,len(WordArray)):
                if WordArray[i] == UserAns:
                    WordArray[i] = ""
        else:
            print("Wrong answer")
        UserAns = input("Your answer: ").lower()

    PercentageCorrect = (UserCorrect/(len(WordArray)-1)) * 100
    print(f"Percentage of correct answers: {PercentageCorrect}")
    UnAnsweredList = ""
    for i in range(1,len(WordArray)):
        if WordArray[i] != "":
            UnAnsweredList += WordArray[i] + ", "
    print(f"Unanswered words: {UnAnsweredList}")

def ReadWords(filename):
    global WordArray
    NumAns = -1
    file = open(filename, "r") 
    dataFetched = file.readline().strip()
    while dataFetched != "":
        WordArray.append(dataFetched) 
        NumAns += 1
        dataFetched = file.readline().strip()
    Play()

difficulties = {
    "easy" : "Easy.txt",
    "medium" : "Hard.txt",
    "hard" : "Hard.txt"
}
print("Difficulties: Easy, Medium, Hard")
UserDifficulty = input("Enter the difficulty you want: ").lower()
ReadWords(difficulties[UserDifficulty])




