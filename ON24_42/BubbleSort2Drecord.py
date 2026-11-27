HighScores = [["","",""] for i in range(7)]

def ReadData(HighScores):
    try:
        filename = "HighScoreTable.txt"
        file = open(filename, "r")
        i = 0
        dataFetched = file.readline().strip()
        while dataFetched != "":
            HighScores[i][0] = dataFetched
            HighScores[i][1] = file.readline().strip()
            HighScores[i][2] = file.readline().strip()
            dataFetched = file.readline().strip()
            i += 1
        return HighScores
    except FileNotFoundError:
        print("File not found")

def OutputHighScores(HighScores):
    for i in range(0, len(HighScores)):
        if HighScores[i][0] == "":
            break
        else:
            print(f"{HighScores[i][0]} reached level {HighScores[i][1]} with a score of {HighScores[i][2]}")

def SortScores(HighScores):
    for o in range(0, len(HighScores) - 1):
        Swap = False
        for i in range(0, len(HighScores) - 1 - o):
            if  (HighScores[i][1] < HighScores[i + 1][1]) or (HighScores[i][1] == HighScores[i + 1][1]) and (HighScores[i][2] < HighScores[i + 1][2]):
                HighScores[i], HighScores[i+1] = HighScores[i+1], HighScores[i]
                Swap = True
        if Swap == False:
            break
    return HighScores

HighScores = ReadData(HighScores)
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)

        

