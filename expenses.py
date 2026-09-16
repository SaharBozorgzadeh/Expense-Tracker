import datetime


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
        #date format should be checked
        #it should be added to the expenses later
        break