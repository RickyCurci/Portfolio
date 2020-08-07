CARS = [
    "FX 305 ZS", [
        "Lambotghini","488 Pista","John Nash"
    ],
    ""
]
INPUT = input("ID (ex. 'AA 000 BB'): ")
class Interface:
    def __init__(self,ID, Mark, Model, Owner):
        self.ID = ID
        self.Mark = Mark
        self.Model = Model
        self.Owner = Owner


    def Page(self):
        return f"""\n____________________________________________________________________________\n| ID            | Mark            | Model              | Owner             |\n----------------------------------------------------------------------------\n|               |                 |                    |                   |\n|   {self.ID}   |   {self.Mark}   |    {self.Model}    |    {self.Owner}   |\n\__________________________________________________________________________/

        """

OUTPUT = Interface(CARS[0],CARS[1][0],CARS[1][1],CARS[1][2])
print(OUTPUT.Page())
