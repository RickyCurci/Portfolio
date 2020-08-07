CARS = [
    "FX 305 ZS", [
        "Ferrari","488 Pista","John Nash"
    ],
    "KJ 589 GH", [
        "Lamborghini", "Sian", "Francisco Gutierrez"
    ],
    "GH 234 SD", [
        "Ford", "GT40", "Paul Walker"
    ],
    "RC 246 GB", [
        "Aston Martin", "Valkrye", "Riccardo Curci"
    ]
]
INPUT = input("ID (ex. 'AA 000 BB'): ")
class Interface:
    def __init__(self,ALL):
        self.ALL = ALL


    def Page(self):
        return f"""\n____________________________________________________________________________\n| ID            | Mark            | Model              | Owner             |\n----------------------------------------------------------------------------\n|               |                 |                    |                   |\n| {self.ALL} |\n\__________________________________________________________________________/

        """
INPUT =  [CARS[0],"|",CARS[1][0],"|",CARS[1][1],"|",CARS[1][2]]
OUTPUT = Interface(INPUT)
print(OUTPUT.Page())
