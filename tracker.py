import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = []
        self.load_expenses()

    def add_expense(self, category, amount, description):
        remaining = self.get_remaining_budget()
        if amount > remaining:
            print(f"⚠️ Warning: You are exceeding your budget by ₹{amount - remaining:.2f}!")
        
        date = datetime.now().strftime("%Y-%m-%d")
        self.expenses.append([date, category, amount, description])
        self.save_expenses()

    def load_expenses(self):
        try:
            with open('expenses.csv', mode='r') as file:
                reader = csv.reader(file)
                self.expenses = list(reader)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open('expenses.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.expenses)

    def get_total_expense(self):
        return sum(float(exp[2]) for exp in self.expenses)

    def get_remaining_budget(self):
        return self.budget - self.get_total_expense()

    def get_savings(self):
        return self.get_remaining_budget()

    def get_summary_by_category(self):
        summary = {}
        for _, category, amount, _ in self.expenses:
            summary[category] = summary.get(category, 0) + float(amount)
        return summary

    def filter_by_category(self, category_name):
        return [exp for exp in self.expenses if exp[1].lower() == category_name.lower()]

    def reset_month(self):
        self.expenses = []
        self.save_expenses()
        print("✅ Monthly data reset successfully!")
