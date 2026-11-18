import json
from expense_models import Expense, InvalidExpenseError  

class ExpenseTracker:
    def __init__(self, filepath: str = "expenses.json"):
        self.filepath = filepath 
        self.expenses: list[Expense] =[]
        self.load_from_file()

    def add_expense(self, title: str,amount: float, category: str)-> Expense:
        clean_title = title.strip()
        clean_cat = category.strip().lower()

        if clean_title == "":
            raise InvalidExpenseError("Title cannot be empty!")
        if amount <= 0:
            raise InvalidExpenseError("Amount must be greater than Zero!")
        if clean_cat == "":
            clean_cat = "general"
        new_expense = Expense(title = clean_title, amount = float(amount),category = clean_cat )
        self.expenses.append(new_expense)
        return new_expense

    def get_total(self)->float:
        total = 0
        for i in self.expenses:
            total += i.amount
            return total

    def get_category_breakdown(self)->dict[str,float]: