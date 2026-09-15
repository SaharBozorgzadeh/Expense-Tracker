# Title
for i in range(20):
    print("=", end="")

print()
print("  EXPENSE TRACKER")
print()

for i in range(20):
    print("=", end="")

print("\n")


# Show menu
def menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Filter Expenses")
    print("7. Statistics")
    print("8. Exit")


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
    

