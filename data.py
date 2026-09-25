import json
from expense import Expense

expensesList = []


def load():
    expensesList.clear()

    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return expensesList

    for item in data:
        expense = Expense(
            item["amount"],
            item["category"],
            item["description"],
            item["date"],
            item["id"]
        )
        expensesList.append(expense)

    return expensesList


def save():
    data = []

    for expense in expensesList:
        data.append({
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "date": expense.date,
            "id": expense.id
        })

    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=4)