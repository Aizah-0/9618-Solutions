class Avatar():
    #private TheName:String
    #private Glasses:Boolean
    #private Hair:String
    #private Age:String

    def __init__(self, TheNameP, GlassesP, HairP, AgeP):
        self.__TheName = TheNameP
        self.__Glasses = GlassesP
        self.__Hair = HairP
        self.__Age = AgeP

    def GetName(self):
        return self.__TheName
    def GetAge(self):
        return self.__Age

    def MeetCriteria(self, WearsGlasses, HairColour):
        if WearsGlasses == self.__Glasses and HairColour == self.__Hair:
            return True
        return False

def LoadAvatars(AvailableAvatars):
    try:
        filename = "AvatarFile.txt"
        file = open(filename, "r")
        for line in file:
            name, glasses, hair, age = line.split(" ")
            if glasses == "True":
                glasses = True
            elif glasses == "False":
                glasses = False
            age = int(age)
            AvailableAvatars.append(Avatar(name, glasses, hair, age))
        return AvailableAvatars
             
    except FileNotFoundError:
        print("File not found")
AvailableAvatars = []

LoadAvatars(AvailableAvatars)

global MatchedAvatars
MatchedAvatars = []


def EnterChoices():
    global MatchedAvatars
    MatchedAvatars = []
    AvailableColors = ["black", "blonde", "brown", "pink", "red", "green"]
    wears_glasses= input("Avatar wears glasses? ").strip()
    hair_color = input("Avatar's hair color? ").strip()
    while (wears_glasses != "yes" and wears_glasses != "no") or (hair_color not in AvailableColors):
        wears_glasses= input("Avatar wears glasses? ").strip()
        hair_color = input("Avatar's hair color? ").strip()
    if wears_glasses== "yes":
        wears_glasses = True
    else:
        wears_glasses = False

    for record in AvailableAvatars:
        if record.MeetCriteria(wears_glasses, hair_color):
            MatchedAvatars.append(record)

EnterChoices()
for avatar in MatchedAvatars:
    print(f"Name: {avatar.GetName()} Age: {avatar.GetAge()}")
print(f"Number of matched: {len(MatchedAvatars)}")



    
