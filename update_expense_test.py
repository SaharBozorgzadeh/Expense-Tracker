import manageExpenses


def test_update_expense(monkeypatch):
    manageExpenses.expensesList.clear()

    expense = manageExpenses.Expense(
        500,
        "Food",
        "Lunch",
        "2026-09-26",
        1
    )

    manageExpenses.expensesList.append(expense)

    inputs = iter([
        "1",           # ID
        "1000",        # new amount
        "Transport",   # new category
        "Taxi",        # new description
        "2026-09-27"   # new date
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    manageExpenses.edit_expenses()

    assert expense.amount == 1000
    assert expense.category == "Transport"
    assert expense.description == "Taxi"
    assert expense.date == "2026-09-27"