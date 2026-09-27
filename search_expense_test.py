import manageExpenses


def test_search_expense(monkeypatch, capsys):
    manageExpenses.expensesList.clear()

    expense = manageExpenses.Expense(
        500,
        "Food",
        "Lunch",
        "2026-09-26",
        1
    )

    manageExpenses.expensesList.append(expense)

    monkeypatch.setattr("builtins.input", lambda _: "Lunch")

    manageExpenses.search_expense()

    captured = capsys.readouterr()

    assert "Lunch" in captured.out