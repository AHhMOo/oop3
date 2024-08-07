class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name 
        self.__allocated_budget = allocated_budget  
        self.__remaining_budget = allocated_budget 

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget < 0:
            raise ValueError("Allocated budget must be a positive number.")
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget  

    def add_expense(self, amount):
        if amount < 0:
            raise ValueError("Expense amount must be a positive number.")
        if amount > self.__remaining_budget:
            raise ValueError("Expense exceeds remaining budget.")
        self.__remaining_budget -= amount

    def display_category_summary(self):
        print(f"Category: {self.__name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")
