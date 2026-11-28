class Character():
    def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP):
        self.__CharacterName = CharacterNameP #string
        self.__DateOfBirth = DateOfBirthP #Date
        self.__Intelligence = IntelligenceP #Real
        self.__Speed = SpeedP #Integer

    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName
    def SetIntelligence(self, IntelligenceU):
        self.__Intelligence = IntelligenceU
    def Learn(self):
        self.__Intelligence *= 1.10
    def ReturnAge(self):
        date, month, year = self.__DateOfBirth.split(" ")
        return 2023 - int(year)

FirstCharacter = Character("Royal", "1 January 2019", 70, 30)
FirstCharacter.Learn()
print(f"Name: {FirstCharacter.GetName()}, Age: {FirstCharacter.ReturnAge()}, Intelligence: {FirstCharacter.GetIntelligence()}")

class MagicCharacter(Character):
    def __init__(self,ElementP, CharacterName, DateOfBirth, Intelligence, Speed):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.__Element = ElementP
    def Learn(self):
        if self.__Element in ["fire", "water"]:
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.__Element == "earth":
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)

FirstMagic = MagicCharacter("fire", "Light", "3 March 2018", 75, 22)
FirstMagic.Learn()
print(f"Name: {FirstMagic.GetName()}, Age: {FirstMagic.ReturnAge()}, Intelligence: {FirstMagic.GetIntelligence()}")


