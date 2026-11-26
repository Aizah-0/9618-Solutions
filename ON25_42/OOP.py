class Bird():
    #Private DistancePerHour :Real
    #Private Species : String
    #Private XPosition : Real
    #Private YPosition : Real

    def __init__(self, DistancePerHourP, SpeciesP, XPositionP, YPositionP):
        self.__DistancePerHour = DistancePerHourP
        self.__Species = SpeciesP
        self.__XPosition = XPositionP
        self.__YPosition = YPositionP

    def GetSpecies(self):
        return self.__Species
    def GetPosition(self):
        return f"X= {self.__XPosition} Y= {self.__YPosition}"
    def Move(self, DirectionTravelled, NumMins):
        DistanceTravelled = (self.__DistancePerHour/60) * NumMins
        if DirectionTravelled == "N":
            self.__YPosition = self.__YPosition + DistanceTravelled
        elif DirectionTravelled == "S":
            self.__YPosition = self.__YPosition - DistanceTravelled
        elif DirectionTravelled == "E":
            self.__XPosition = self.__XPosition + DistanceTravelled
        elif DirectionTravelled == "W":
            self.__XPosition = self.__XPosition - DistanceTravelled


FirstBird = Bird(71.0, "Cockatiel",500,500)
SecondBird = Bird(56.0, "Macaw",500,500)

print(f"First bird {FirstBird.GetSpecies} currently at: {FirstBird.GetPosition()}")
print(f"Second bird {SecondBird.GetSpecies} currently at: {SecondBird.GetPosition()}")


BirdChosen = input("Select a Bird: ")
while BirdChosen != "Cockatiel" and BirdChosen != "Macaw":
    BirdChosen = input("Select a Bird: ")

DirectionMoved = input("Enter the direction to move: ")
while DirectionMoved not in ["N", "S", "W", "E"]:
    DirectionMoved = input("Enter the direction to move: ")

try:
    TimeMoved = float(input("Enter to the nearest minute, time for which the bird moved: "))
    while not 0 <= TimeMoved <= 500:
        TimeMoved = float(input("Enter to the nearest minute, time for which the bird moved: "))
except ValueError:
    print("Invalid, time must be between 0 and 500")


if BirdChosen == "Cockatiel":
    FirstBird.Move(DirectionMoved,TimeMoved)
    print(f"First bird now at: {FirstBird.GetPosition()}")
elif BirdChosen == "Macaw":
    SecondBird.Move(DirectionMoved,TimeMoved)
    print(f"Second bird now at: {SecondBird.GetPosition()}")


