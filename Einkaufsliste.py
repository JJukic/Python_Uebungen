# Einkaufsliste Menü

#DB
einkaufsliste = []

while True:
    print("\nWas möchtest du tun ?")
    print("1-Artikel hinzufügen")
    print("2-Liste anzeigen")
    print("3-Beenden")

    Auswahl = input("Deine Auswahl:")

    if Auswahl == "1":
        artikel = input("Gib den Artikel ein um ihn hinzuzufügen: ")
        if artikel.strip(): # strip ignoriert leere Eingaben
            einkaufsliste.append(artikel)
            print(f"'{artikel}' wurde zur Einkaufsliste hinzugefügt.")
        else:
            print("Kein Artikel eingegeben.")

    elif Auswahl == "2":
        print("Deine Einkaufsliste")
        if not einkaufsliste:
            print("Die Liste ist leer.")
        else:
            for nummer, eintrag in enumerate(einkaufsliste, start=1):
                print(f"{nummer}. {eintrag}")

    elif Auswahl == "3":
        print("Bis zum nächsten Mal")
        break

    else:
        print("Ungültige Eingabe, bitte wähle Sie 1,2 oder 3 aus.")
