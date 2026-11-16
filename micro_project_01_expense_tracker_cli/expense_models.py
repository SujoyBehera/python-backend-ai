from dataclasses import dataclass
class InvalidExpenseError(ValueError):
    pass

@dataclass
class Expense:
    title: str
    amount: float
    category: str


    def to_dict(self):
        return {"title":self.title,"amount":self.amount,"category":self.category}
    