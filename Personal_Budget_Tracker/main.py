
import json
from datetime import datetime
from budget_utils import group_by_category, calculate_totals, save_transaction, load_transactions

class Transaction:
    def __init__(self, category, amount):
        self.date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount
        }

def main():
    
    print("Welcome to Personal Budget Tracker\n")
    while True:
        category = input("Enter category (e.g., food, transport and 'done' to exit): ").lower()
        if category == 'done':
            break
        if not category:
            print("Category cannot be blank")
            continue
        category = " ".join(category.split())
        try:
            amount = float(input("Enter amount: "))
        except:
            print("Invalid Input: Must be a number")
            continue
        
        transaction = Transaction(category, amount)
        transaction_to_dict = transaction.to_dict()
        save_transaction(transaction_to_dict)

    grouped = group_by_category()
    print(grouped)
    totals = calculate_totals(grouped)
    print(totals)

    if not totals:
        print("--- No Budget Record ---")
    else:
        print("\nExpense Summary:")
        for category, total in totals.items():
            print(f"{category.capitalize()}: ${total:.2f}")

if __name__ == '__main__':
    main()
