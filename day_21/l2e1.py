# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and 
# it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
# Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self,firstname="name",lastname="lastName",
                incomes={10000:"for job",200:"for commission"},expenses={1000:"for chair",200:"for food"}):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
        
    def total_income(self):
        result = 0
        for income in self.incomes:
            result+=income
        return result
    def total_expense(self):
        result = 0
        for expense in self.expenses:
            result+=expense
        return result
    def account_info(self):
        return f"{self.firstname} {self.lastname} earns {self.total_income()} and spends {self.total_expense()}"
    def add_income(self,amount,reason):
        self.incomes[amount] = reason
    def add_expense(self,amount,reason):
        self.expenses[amount] = reason
    def account_balance(self):
        return self.total_income()-self.total_expense()