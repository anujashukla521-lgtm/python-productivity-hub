expenses = []


def add_expense(expense):
    expense_name = input("Enter expense: ").strip()
    if not expense_name:
        print("Vacant spaces are not allowed")
        return

    try:

        amount = float(input("Enter amount: "))
    except ValueError:
        print("Non numeric constant")
        return

    expense.append({
        "expense": expense_name,
        "amount": amount
    })

   


def view_expenses(expense):
    if not expense:
        print("There are no expenses")
        return 

    for index, item in enumerate(expense, start=1):
        print(f"{index}. {item['expense']}- Rs. {item['amount']}")



def delete_expense(expense):
    if not expense:
        print("No expense available")
        return
    
    for index, item in enumerate(expense,start=1):
        print(f"{index}. {item['expense']}- Rs. {item['amount']}")


    try:
        choice = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid choice")
        return

    if choice>0 and choice <= len(expense):
        choice = choice-1
        expense.pop(choice)
        print("Expense deleted successfully")
    else:
        print("Number out of range")


def total_expenses(expense):
    total = 0
    for cost in expense:
        total+=cost['amount']

    print(f"Total expenses: Rs. {total}")



def expense_menu():
    while True:
        try:
            choice = int(input("Expense Menu\n1-Add Expense\n2-View Expenses\n3-Delete Expense\n4-Total expenses\n5-Back\n"))
        except ValueError:
            print("Invalid input")
            continue


        match choice:
            case 1:
                add_expense(expenses)

            case 2:
                view_expenses(expenses)

            case 3:
                delete_expense(expenses)

            case 4:
                total_expenses(expenses)

            case 5:
                break
            case _:
                print("Wrong choice")

if __name__=="__main__":
    expense_menu()
