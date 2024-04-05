# Program for the Expense Tracker

import os
import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists("expenses.txt"):
            with open("expenses.txt", "r") as file:
                for line in file:
                    category, date_str, amount = line.strip().split(",")
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                    self.add_expense(category, date, float(amount))

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for category, category_expenses in self.expenses.items():
                for date, amount in category_expenses.items():
                    file.write(f"{category},{date.strftime('%Y-%m-%d')},{amount}\n")

    def add_expense(self, category, date, amount):
        if category in self.expenses:
            if date in self.expenses[category]:
                self.expenses[category][date] += amount
            else:
                self.expenses[category][date] = amount
        else:
            self.expenses[category] = {date: amount}
        self.save_expenses()

    def delete_expense(self, category, date):
        if category in self.expenses and date in self.expenses[category]:
            del self.expenses[category][date]
            self.save_expenses()

    def show_expenses(self, start_date=None, end_date=None):
        total_expense = 0
        print("Expenses:")
        for category, category_expenses in self.expenses.items():
            print(f"{category}:")
            for date, amount in category_expenses.items():
                if (start_date is None or start_date <= date) and (end_date is None or date <= end_date):
                    print(f"{date}: ${amount:.2f}")
                    total_expense += amount
            print()
        print(f"Total: ${total_expense:.2f}")

def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense\n2. Delete Expense\n3. Show Expenses\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            category = input("Enter category: ")
            date = get_date_input("Enter date")
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, date, amount)
            print("Expense added successfully!")
        elif choice == "2":
            category = input("Enter category: ")
            date = get_date_input("Enter date")
            tracker.delete_expense(category, date)
            print("Expense deleted successfully!")
        elif choice == "3":
            print("\n1. Show all expenses\n2. Show expenses for a specific time period\n")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                tracker.show_expenses()
            elif sub_choice == "2":
                start_date = get_date_input("Enter start date")
                end_date = get_date_input("Enter end date")
                tracker.show_expenses(start_date, end_date)
            
            else:
                print("Invalid choice.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
