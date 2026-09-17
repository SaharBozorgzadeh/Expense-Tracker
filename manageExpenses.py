import datetime
from data import expensesList
from expense import Expense
from Menu import menu


def add_expenses():

    while True:

        print("Please enter the suitable answer for each option:")

        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be bigger than 0")
                continue

        except ValueError:
            print("Amount must be a number!")
            continue

        category = input("Category: ")

        if not category.strip():
            print("Category cannot be empty.")
            continue

        description = input("Description: ")

        date = input("Date: ")
        if not date.strip():
            date = datetime.date.today().isoformat()

        # TODO: Validate the date format

        # Add the new expense to the list
        new_id = len(expensesList) + 1
        expense = Expense(amount, category, description, date, new_id)
        expensesList.append(expense)
        menu()
        break


def view_expenses():
    if not expensesList:
        print("No expenses found.")
    else:
        print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<12}{'Description'}")
        for expense in expensesList:
            print(
                f"{expense.id:<5}{expense.date:<15}{expense.category:<15}{expense.amount:<12}{expense.description}"
            )
    menu()
    return


def edit_expenses():
    # Find the expense by ID
    expense_id = int(input("Please enter expense ID: "))
    expense = next((i for i in expensesList if i.id == expense_id), None)
    if expense is None:
        print("There is no such expense")
        menu()
        return

    # Change the amount
    print(f"Current Amount: {expense.amount}")
    try:
        new_amount = float(input("New amount: "))

        if new_amount <= 0:
            print("Amount must be bigger than 0, editing failed")
            menu()
            return
        expense.amount = new_amount
    except ValueError:
        print("Amount must be a number!, editing failed")
        menu()
        return
    

    # Change the category
    print(f"Current category: {expense.category}")
    new_category = input("New category: ")

    if not new_category.strip():
        print("Category cannot be empty.")
        menu()
        return
    expense.category = new_category

    # Change the description
    print(f"Current description: {expense.description}")
    new_description = input("Description: ")
    expense.description = new_description

    # Change the date
    print(f"Current date: {expense.date}")
    new_date = input("Date: ")
    if not new_date.strip():
        new_date = datetime.date.today().isoformat()
    expense.date = new_date

    menu()
    return

def delete_expenses() :
    expense_id = int(input("Please enter expense ID: "))
    expense = next((i for i in expensesList if i.id == expense_id), None)
    if expense is None:
        print("There is no such expense")
        menu()
        return
    answer = input("Are you sure?(y/n)")
    if answer.lower() == 'y':
        expensesList.remove(expense)
        print("Expense was deleted successfully!")
    menu()
    return

