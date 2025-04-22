# Liste von Zimmern:
zimmer_liste = []

#Liste der Gäste
gaeste_liste = []

#Liste Buchungen
buchungen_liste = []

class Zimmer:
    def __init__(self, zimmernummer: int, zimmer_typ: str, preis: float):
        self.zimmernummer = zimmernummer
        self.zimmer_typ = zimmer_typ
        self.preis = preis

    def __str__(self):
        return f"{self.zimmernummer} {self.zimmer_typ} {self.preis}"

class Gast:
    def __init__(self, vorname: str, nachname: str):
        self.vorname = vorname
        self.nachname = nachname

    def __str__(self):
        return f"{self.vorname} {self.nachname}"

class Buchung:
    def __init__(self, gast: Gast, zimmer: Zimmer, check_in: str, check_out: str):
        self.gast = gast
        self.zimmer = zimmer
        self.check_in = check_in
        self.check_out = check_out

    def __str__(self):
        return f"{self.gast.vorname}{self.gast.nachname} bucht Zimmer{self.zimmer.zimmernummer}, {self.zimmer.zimmer_typ}, {self.zimmer.preis:.2f} von {self.check_in} bis {self.check_out}."

def main_menu():
    print("\n========Hotel Menü========")
    print("1. Zimmer hinzufügen")
    print("2. Gäste hinzufügen")
    print("3. Buchung erstellen")
    print("4. Alle Buchungen anzeigen")
    print("5. Alle Zimmer anzeigen")
    print("6. Alle Gäste anzeigen")
    print("7. Gast bearbeiten")
    print("8. Gast löschen")
    print("9. Beenden")

    auswahl = input("Wähle eine Option (1-9): ")
    return auswahl

while True:
    auswahl = main_menu()

    if auswahl == "1":
        print("Wieviele Zimmer möchtest du hinzufügen ?")
        try:
            anzahl = int(input("Anzahl Zimmer eingeben: "))
            if not anzahl:
                raise ValueError("Eingabe darf nicht leer sein.")
            anzahl = int(anzahl)
        except ValueError as e:
            print(f"Ungültige Eingabe: {e}.")
            continue
        neue_zimmer = []
        for index in range(anzahl):
            zimmernummer = int(input("Zimmernummer: "))
            zimmer_typ = input("Zimmer Typ: ")
            preis = float(input("Zimmerpreis pro Nacht: "))
            zimmer = Zimmer(zimmernummer, zimmer_typ, preis)
            zimmer_liste.append(zimmer)
            neue_zimmer.append(zimmer)
            print(f"\nhinzugefügte Zimmer {zimmer.zimmernummer}, {zimmer.zimmer_typ}, {zimmer.preis:.2f} CHF/Nacht hinzugefügt")
        print("\nAlle neu hinzugefügten Zimmer:")
        for index, z in enumerate(neue_zimmer, start=1):
            print(f"{index}. Zimmer: {z.zimmernummer}, {z.zimmer_typ}, {z.preis:.2f} CHF/Nacht.")

    elif auswahl == "2":
        vorname = input("Vorname: ")
        nachname = input("Nachname: ")
        gast = Gast(vorname, nachname)
        gaeste_liste.append(gast)
        print(f"\nGast {gast.vorname}, {gast.nachname} hinzugefügt")

    elif auswahl == "3":
        if not gaeste_liste or not zimmer_liste:
            print("Bitte zuerst Gäste und Zimmer hinzufügen")
        else:
            print("\nGast wählen: ")
            for i, g in enumerate(gaeste_liste, start=1):
                print(f"{i}. Gast {g.vorname} {g.nachname}")
            gast_index = int(input("Wähle den Gast (Nummer): ")) - 1
            gast = gaeste_liste[gast_index]

            print("\nZimmer wählen:")
            for i, z in enumerate(zimmer_liste, start=1):
                print(f"{i}. Zimmer {z.zimmernummer}, {z.zimmer_typ}, {z.preis:.2f} CHF/Nacht")
            zimmer_index = int(input("Wähle die Zimmernummer: ")) -1
            zimmer = zimmer_liste[zimmer_index]

            check_in = input("Check-in (YYYY-MM-DD): ")
            check_out = input("Check-out (YYYY-MM-DD): ")

            buchung = Buchung(gast, zimmer, check_in, check_out)
            buchungen_liste.append(buchung)
            print("Buchung erstellt")

    elif auswahl == "4":
        # Alle Buchungen anzeigen
        if not buchungen_liste:
            print("Keine Buchungen vorhanden.")
        else:
            print("\nAlle Buchungen:")
            for i, b in enumerate(buchungen_liste, start=1):
                print(f"{i}. {b}")

    elif auswahl == "5":
        if not zimmer_liste:
            print("Keine Zimmer vorhanden. ")
        else:
            print("\nAlle Zimmer:")
            for i, z in enumerate(zimmer_liste, start=1):
                print(f"{i}. Zimmer{z.zimmernummer}, {z.zimmer_typ}, {z.preis:.2f} CHF")

    elif auswahl == "6":
        if not gaeste_liste:
            print("Keine Gäste vorhanden. ")
        else:
            for i, g in enumerate(gaeste_liste, start=1):
                print(f"{i}. Gast: {g}")

    elif auswahl == "7":
        if not gaeste_liste:
            print("Keine Gäste vorhanden.")
        else:
            print("\nGäste: ")
            for i, g in enumerate(gaeste_liste, start=1):
                print(f"{i}. Gast {g.vorname}, {g.nachname}")
            try:
                index = int(input("Welchen Gast (Nummer) möchtest du bearbeiten ?")) -1
                if 0 <= index < len(gaeste_liste):
                    neuer_vorname = input("Neuer Vorname (leer zum beibehalten): ")
                    neuer_nachname = input("Neuer Nachname (leer zum beibehalten): ")

                    if neuer_vorname:
                        gaeste_liste[index].vorname = neuer_vorname
                    if neuer_nachname:
                        gaeste_liste[index].nachname = neuer_nachname

                    print("Gast erfolgreich bearbeitet.")
                    print(f"{index+1}. {gaeste_liste[index].vorname} {gaeste_liste[index].nachname}")
                else:
                    print("Ungültige Nummer.")
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")


    elif auswahl == "8":
        if not gaeste_liste:
            print("Keine Gäste vorhanden. ")
        else:
            print("\nGäste: ")
            for index, g in enumerate(gaeste_liste, start=1):
                print(f"{index}. Gast {g.vorname}, {g.nachname}")
            try:
                index = int(input("Welchen Gast (Nummer) möchtest du löschen?")) -1
                if 0<= index < len(gaeste_liste):
                    geloeschter_gast = gaeste_liste.pop(index)
                    print(f"Gelöschter Gast: {geloeschter_gast.vorname}, {geloeschter_gast.nachname}")
                else:
                    print("Ungültige Nummer")
            except ValueError:
                print("Bitte eine gültige Zahl eingeben")


    elif auswahl == "9":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Eingabe. Bitte 1–9 wählen.")