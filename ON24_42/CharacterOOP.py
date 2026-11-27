class EventItem():
    def __init__(self, EventNameP, TypeP, DifficultyP):
        self.__EventName = EventNameP #String #Private
        self.__Type = TypeP #String # Private
        self.__Difficulty = DifficultyP #Integer #Pivate
    def GetName(self):
        return self.__EventName
    def GetDifficulty(self):
        return self.__Difficulty
    def GetEventType(self):
        return self.__Type

Group = []
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mil run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on Wall", "jump", 4))

class Character():
    def __init__(self, CharacterNameP, JumpP, SwimP, RunP, DriveP):
        self.__CharacterName = CharacterNameP #String # Private
        self.__Jump = JumpP #Intger # Private
        self.__Swim = SwimP #Intger # Private
        self.__Run = RunP #Intger # Private
        self.__Drive = DriveP #Intger # Private
    def GetName(self):
        return self.__CharacterName
    def CalculateScore(self, EventType, EventDifficulty):
        skills = {
            "jump" : self.__Jump,
            "swim" : self.__Swim,
            "run"  : self.__Run,
            "drive": self.__Drive
        }
        percentages = {
            "1" : 80,
            "2" : 60,
            "3" : 40,
            "4" : 20
        }
        SkillLevel = skills[EventType.lower()]
        if SkillLevel >= EventDifficulty:
            return 100
        SkillDifference = EventDifficulty - SkillLevel
        return percentages[str(SkillDifference)]

CharacterT = Character("Tarz",5,3,5,1)
CharacterG = Character("Geni",2,2,3,4)
CharacterTScore = 0
CharacterGScore = 0

for item in Group:
    EventType = item.GetEventType()
    EventDifficulty = item.GetDifficulty()
    EventName = item.GetName()
    CharacterTChance = CharacterT.CalculateScore(EventType, EventDifficulty)
    CharacterGChance = CharacterG.CalculateScore(EventType, EventDifficulty)
    if CharacterTChance > CharacterGChance:
        CharacterTScore += 1
        print(f"{CharacterT.GetName()} has won {EventName} of type {EventType}")
    elif CharacterGChance > CharacterTChance:
        CharacterGScore += 1
        print(f"{CharacterG.GetName()} has won {EventName} of type {EventType}")
    else:
        print(f"{EventType} is a draw")

if CharacterTScore > CharacterGScore:
    print(f"{CharacterT.GetName()} has the most points for the group. Score: {CharacterTScore}")
elif CharacterGScore > CharacterTScore:
    print(f"{CharacterG.GetName()} has the most points for the group. Score: {CharacterGScore}")
else:
    print(f"The group is a draw")

