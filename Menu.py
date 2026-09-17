import manageExpenses

def menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Filter Expenses")
    print("7. Statistics")
    print("8. Exit")


def start():
    while True:
        menu()
        try:
            choice = int(input("Choose an option: "))

            if choice > 8 or choice < 1:
                print("Please enter a number from the menu.\n")
                continue

            print("Opening your selected option...")
            break

        except ValueError:
            print("Please enter a valid number from the menu.\n")

    option_opener(choice)
    return

def option_opener(choice):
    match choice:
        case 1:
            manageExpenses.add_expenses()
        case 2:
            manageExpenses.view_expenses()
        case 3:
            manageExpenses.edit_expenses()
        case 4:
            manageExpenses.delete_expenses()
        case 5:
            manageExpenses.search_expense()
        case 6:
            manageExpenses.filter_expenses()
        case 7:
            # TODO: statistics
            pass
        case 8:
            print("Goodbye!")
            return
    start()
    return
# Title
for i in range(20):
    print("=", end="")

print()
print("  EXPENSE TRACKER")
print()

for i in range(20):
    print("=", end="")

print("\n")
start()