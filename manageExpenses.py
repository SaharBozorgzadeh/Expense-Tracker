import datetime
from data import expensesList
from expense import Expense


def addExpenses():

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
        break
