import manageExpenses


def test_delete_expense(monkeypatch):
    manageExpenses.expensesList.clear()

    expense = manageExpenses.Expense(
        500,
        "Food",
        "Lunch",
        "2026-09-26",
        1
    )

    manageExpenses.expensesList.append(expense)

    inputs = iter(["1", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    manageExpenses.delete_expenses()

    assert len(manageExpenses.expensesList) == 0