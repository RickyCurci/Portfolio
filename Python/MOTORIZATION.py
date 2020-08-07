CARS = [
    "FX 305 ZS" [
        "Ferrari","488 Pista","John Nash"
    ],
]
INPUT = input("ID (ex. 'AA 000 BB'): ")
class Interface:
    def __init__(self,ID, Mark, Model, Owner):
        self.ID = ID
        self.Mark = Mark
        self.Model = Model
        self.Owner = Owner
 

    def Page(self):
        return f"""               CHEAPEST HILL MOTORIZATION\n________________________________________________________________________\n| ID           | Mark        | Model              | Owner              |\n
        ------------------------------------------------------------------------\n
        |              |             |                    |                    |\n
        | {self.ID}   | {self.Mark} | {self.Model}       | {self.Owner}       |\n
        ________________________________________________________________________"""

OUTPUT = Interface(CARS[INPUT],CARS[INPUT][0],CARS[INPUT][1],CARS[INPUT][2])
print(OUTPUT.Page())
