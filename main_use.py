from budget_category import BudgetCategory

def main():
    food_category = BudgetCategory("Food", 500)
    
    print("Initial Budget Details:")
    food_category.display_category_summary()
    
    print("\nAdding expenses...")
    try:
        food_category.add_expense(100)
        food_category.add_expense(50)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nUpdated Budget Details:")
    food_category.display_category_summary()

    print("\nAttempting to add an expense that exceeds the remaining budget...")
    try:
        food_category.add_expense(400)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nFinal Budget Details:")
    food_category.display_category_summary()
main()
