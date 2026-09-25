import datetime
from data import expensesList
from expense import Expense


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
        break
    return

def view_expenses():
    if not expensesList:
        print("No expenses found.")
    else:
        print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<12}{'Description'}")
        for expense in expensesList:
            print(
                f"{expense.id:<5}{expense.date:<15}{expense.category:<15}{expense.amount:<12}{expense.description}"
            )
    return


def edit_expenses():
    # Find the expense by ID
    expense_id = int(input("Please enter expense ID: "))
    expense = next((i for i in expensesList if i.id == expense_id), None)
    if expense is None:
        print("There is no such expense")
        return

    # Change the amount
    print(f"Current Amount: {expense.amount}")
    try:
        new_amount = float(input("New amount: "))

        if new_amount <= 0:
            print("Amount must be bigger than 0, editing failed")
            return
        expense.amount = new_amount
    except ValueError:
        print("Amount must be a number!, editing failed")
        return
    

    # Change the category
    print(f"Current category: {expense.category}")
    new_category = input("New category: ")

    if not new_category.strip():
        print("Category cannot be empty.")
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

    print("Expense was edited successfully!")
    return

def delete_expenses() :
    expense_id = int(input("Please enter expense ID: "))
    expense = next((i for i in expensesList if i.id == expense_id), None)
    if expense is None:
        print("There is no such expense")
        return
    answer = input("Are you sure?(y/n)")
    if answer.lower() == 'y':
        expensesList.remove(expense)
        print("Expense was deleted successfully!")
    return

def search_expense():
    description = input("Enter expense's description: ")

    results = [i for i in expensesList if i.description == description]
    if not results:
        print("There is no such expense")
    else:
        print(results)
    return

def filter_expenses():
    print("choose based on what you want to filter the expenses:")
    print("1.Amount")
    print("2.Date")
    print("3.Category")
    print("4.back")
    try:
        choice = int(input("Choose an option: "))
    
        if choice > 4 or choice < 1:
            print("Please enter a number from the menu.\n")
            return
    
    except ValueError:
        print("Please enter a valid number from the menu.\n")
        return
    
    if choice == 1:
        filter_by_amount()
    elif choice == 2:
        filter_by_date()
    elif choice == 3:
        filter_by_category()

    return

# Filter helper functions

def filter_by_amount():
    try:
        max_amount = float(input("Enter maximum range:"))
        min_amount = float(input("Enter minimum range"))
    except ValueError:
        print("you should enter a number only")
        filter_expenses()
        return
  
    results = [i for i in expensesList if i.amount <= max_amount and i.amount >= min_amount]
    if not results:
        print("There is no such expense")
    else:
        for i in results:
            print(i)
    return

def filter_by_date():
    date = input("Enter date:")
    results = [i for i in expensesList if i.date == date]
    if not results:
        print("There is no such expense")
    else:
        for i in results:
            print(i)
    return

def filter_by_category():
    category = input("Enter category:")
    results = [i for i in expensesList if i.category == category]
    if not results:
        print("There is no such expense")
    else:
        for i in results:
            print(i)
    return

def show_stats_title():
    for i in range(20):
        print("=", end="")

    print()
    print("  Statistics")
    print()

    for i in range(20):
        print("=", end="")

    print("\n")


def statistics():
    show_stats_title()
    if not expensesList:
        print("No expenses found")
        return
    totalExpenses = 0
    highest_expense = expensesList[0]
    lowest_expense = expensesList[0]
    for expense in expensesList:
        totalExpenses += expense.amount
        if expense.amount > highest_expense.amount:
            highest_expense = expense
        if expense.amount < lowest_expense.amount:
                lowest_expense = expense

    print(f"Total Expenses: {totalExpenses}")
    print(f"Number of Expenses: {len(expensesList)}")
    print(f"Average Expense: {totalExpenses/len(expensesList)}")
    print("\n")
    print("Highest Expense:")
    print(highest_expense.amount,"-", highest_expense.category)
    print("\n")
    print("Lowes Expense:")
    print(lowest_expense.amount ,"-", lowest_expense.category)
    category_statistics()
    daily_spending()
    monthly_spending()

def category_statistics();
    spending_by_category = {}

    for expense in expensesList:
        if expense.category not in spending_by_category:
            spending_by_category[expense.category] = 0

        spending_by_category[expense.category] += expense.amount

    for category, amount in spending_by_category.items():
        print(category, amount)

def daily_spending():
    daily_total = 0

    for expense in expensesList:
        if expense.date == datetime.date.today().isoformat():
            daily_total += expense.amount

    print(f"Daily spending: {daily_total}")

def monthly_spending():
    monthly_expenses = {}

    today = datetime.date.today()

    for expense in expensesList:
        expense_year = int(expense.date[:4])
        expense_month = int(expense.date[5:7])

        if expense_year == today.year and expense_month == today.month:
            if expense.date not in monthly_expenses:
                monthly_expenses[expense.date] = 0

            monthly_expenses[expense.date] += expense.amount

    for date, amount in monthly_expenses.items():
        print(date, amount)