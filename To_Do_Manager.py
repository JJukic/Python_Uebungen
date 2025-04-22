#Liste der Aufgaben
tasks = []

def show_menu():
    print("\n1. Aufgabe hinzufügen")
    print("2. Alle Aufgaben anzeigen")
    print("3. Aufgabe als erledigt markieren")
    print("4. Beenden")

def add_tasks():
    text = input("Aufgabe eingeben: ")
    tasks.append({"text": text, "done": False})
    print(f"Aufgabe '{text}' hinzugefügt.")

def list_tasks():
    if not tasks:
        print("Keine Aufgaben vorhanden")
        return
    for index, task in enumerate(tasks, start=1):
        status = " ✓ " if task["done"] else "  "
        print(f"{index}. [{status}] {task['text']}")

def complete_tasks():
    list_tasks()
    if not tasks:
        return
    try:
        nummer = int(input("Nummer der zu markierenden Aufgabe: "))
        tasks[nummer-1]["done"] = True
        print(f"Aufgabe '{tasks[nummer-1]['text']}' als erledigt markiert. ")
    except ValueError:
        print("Bitte gib eine Zahl ein.")
    except IndexError:
        print("Diese Zahl gibt es nicht.")



if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Wähle 1-4: ")

        if choice == "1":
            add_tasks()

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            complete_tasks()

        elif choice == "4":
            print("Auf Wiedersehen")
            break
        else:
            print("Ungültige Eingabe, bitte geben Sie eine Zahl zwischen 1-4 ein.")
