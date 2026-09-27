import manageExpenses


def test_add_expense(monkeypatch):
    manageExpenses.expensesList.clear()

    inputs = iter([
        "500",
        "Food",
        "Lunch",
        "2026-09-26"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    manageExpenses.add_expenses()

    assert len(manageExpenses.expensesList) == 1
    assert manageExpenses.expensesList[0].amount == 500
    assert manageExpenses.expensesList[0].category == "Food"