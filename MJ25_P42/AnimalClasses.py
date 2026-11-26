class Animal():
    def __init__(self, NameP, SoundP, SizeP, IntellegenceP):
        self.__Name = NameP #String
        self.__Sound = SoundP #String
        self.__Size = SizeP #Integer
        self.__Intellegence = IntellegenceP #Integer

    def Description(self):
        StringToReturn = f"The animal's name is {self.__Name}, it makes a {self.__Sound}, its size is {self.__Size} and its intelligence level is {self.__Intellegence}"
        return StringToReturn

class Parrot(Animal):
    def __init__(self, NameP, SoundP, SizeP, IntellegenceP, WingSpanP, NumberWordsP):
        super().__init__(NameP, SoundP,SizeP,IntellegenceP)
        self.__WingSpan = WingSpanP #integer
        self.__NumberWords = NumberWordsP #integer 

    def Description(self):
        StringToReturn = f"{super().Description()}. It has a wingspan of {self.__WingSpan}cm and can say {self.__NumberWords} words."
        return StringToReturn

    def ChangeNumberWords(self, NumberToAdd):
        self.__NumberWords +=  NumberToAdd

class Wolf(Animal):
    def __init__(self, NameP, SoundP, SizeP, IntellegenceP, TerritoySizeP):
        super().__init__(NameP, SoundP, SizeP, IntellegenceP)
        self.__TerritorySize = TerritoySizeP #integer

    def Description(self):
        StringToReturn = f"{super().Description()}. Its territory is {self.__TerritorySize} square miles."
        return StringToReturn

    def SetTerritorySize(self, NumberToAdd):
        self.__TerritorySize += NumberToAdd

AnimalParrot = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
AnimalWolf = Wolf("Nighteyes", "Howl", 8, 7, 100)
AnimalHorse = Animal("Copper", "Neigh", 10, 6)

AnimalWolf.SetTerritorySize(-20)
AnimalParrot.ChangeNumberWords(2)
print(AnimalParrot.Description)
print(AnimalWolf.Description)
print(AnimalHorse.Description)
