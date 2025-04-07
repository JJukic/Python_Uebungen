# Diese Übung ist zum Lernen von Klassen und Konstruktoren

class Auto:
    def __init__(self, marke, baujahr, km):
        self.marke = marke
        self.baujahr = baujahr
        self.km = kilometer

    def beschreibe(self):
        print(f"Das Auto hat die Marke {self.marke} und ist aus dem Jahr {self.baujahr} und hat {self.km} km.")

autos = []
anzahl = int(input("Wie viele Autos möchtest du hinzufügen ?"))

for i in range(anzahl):
    print(f"\nAuto {i+1}:")
    marke = input("Marke: ")
    while True:
        try:
            baujahr = int(input("Baujahr: "))
            break
        except ValueError:
            print(f"Eingabe falsch, bitte nur ganze Zahlen eingeben")

    while True:
        try:
            kilometer = int(input("Kilometer: "))
            break
        except ValueError:
            print(f"Eingabe falsch, bitte nur ganze Zahlen eingeben")

    auto = Auto(marke, baujahr, kilometer)
    autos.append(auto)


print(f"\nDeine Autos in der Liste:")
#autos = [
#    Auto("Audi", 2019),
#    Auto("BMW", 2022),
#    Auto("Ferrari", 2023),
#    Auto("Tesla", 2020)
#]

#auto1 = Auto("Audi", 2019)
#auto2 = Auto("BMW", 2022)
#auto3 = Auto("Ferrari", 2023)
#auto1.beschreibe()
#auto2.beschreibe()
#auto3.beschreibe()

for index, auto in enumerate(autos, start=1):       # enumerate mit start=1 beginnt von 1 und nicht von 0
    print(f"{index}.", end="")                      # end="" verhindert den Zeilenumbruch
    auto.beschreibe()
