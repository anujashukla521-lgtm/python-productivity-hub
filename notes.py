notebooks = []
def add_note(notebook):
    words = input("Enter notes: ").strip()
    if not words:
        print("Vacant spaces are not allowed")
        return

    notebook.append(words)
    print("Note added successfully")
    

def view_notes(notebook):
    if not notebook:
        print("No notes are there")
        return 


    for index, words in enumerate(notebook,start=1):
        print(f"{index}. {words}")

def delete_note(notebook):
    if not notebook:
        print("No notes are there")
        return
    
    for index, words in enumerate(notebook,start=1):
        print(f"{index}. {words}")
    try:
        choice = int(input("Enter note number to delete: "))
    except ValueError:
        print("Invalid choice")
        return

    if choice>0 and choice <= len(notebook):
        choice = choice-1
        notebook.pop(choice)
        print("Note deleted successfully")
    else:
        print("Number out of range")

def notes_menu():
    while True:
        try:
            choice = int(input("Notes Menu\n1-Add notes\n2-View notes\n3-Delete notes\n4-Back\n"))
        except ValueError:
            print("Invalid input")
            continue

        match choice:
            case 1:
                add_note(notebooks)
            case 2:
                view_notes(notebooks)
            case 3:
                delete_note(notebooks)
            case 4:
                break
            case _:
                print("Wrong choice")


if __name__=="__main__":
    notes_menu()