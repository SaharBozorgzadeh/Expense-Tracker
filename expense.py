class Expense:

    def __init__(self, amount, category, description, date, id):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.id = id
    
    def __str__(self):
        return f"{self.id} {self.date} {self.category} {self.amount} {self.description}"