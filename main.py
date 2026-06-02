import notes 
import tasks
import password_checker
import expense_tracker

def main():
    while True:
        try:
            choice = int(input("Enter your choice:\n1-Notes\n2-Tasks\n3-Expenses\n4-Password checker\n5-Exit\n"))
        except ValueError:
            print("Invalid input")
            continue

        match choice:
            case 1:
                notes.notes_menu()
            case 2:
                tasks.tasks_menu()

            case 3:
                expense_tracker.expense_menu()

            case 4:
                password_checker.password_menu()


            case 5:
                print("Exit")
                break
            case _:
                print("Wrong choice")


if __name__=="__main__":
    main()