from tracker import ExpenseTracker
from visualizer import plot_expense_summary

def main():
    print("=== Welcome to Expense Tracker ===")
    budget = float(input("Set your monthly budget: ₹ "))

    tracker = ExpenseTracker(budget)

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. View Summary Report")
        print("3. View Remaining Budget")
        print("4. Filter Expenses by Category")
        print("5. Reset Monthly Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (e.g. Food, Travel): ")
            amount = float(input("Enter amount: ₹ "))
            description = input("Enter description: ")
            tracker.add_expense(category, amount, description)

        elif choice == '2':
            total_spent = tracker.get_total_expense()
            savings = tracker.get_savings()
            summary = tracker.get_summary_by_category()

            print(f"\n📊 Total Spent: ₹{total_spent:.2f}")
            print(f"💰 Savings: ₹{savings:.2f}")
            print("\nCategory-wise Summary:")
            for cat, amt in summary.items():
                print(f"  - {cat}: ₹{amt:.2f}")

            plot_expense_summary(summary)

        elif choice == '3':
            print(f"💼 Remaining Budget: ₹{tracker.get_remaining_budget():.2f}")

        elif choice == '4':
            category = input("Enter category to filter: ")
            filtered = tracker.filter_by_category(category)
            if filtered:
                print(f"\nExpenses in '{category}':")
                for exp in filtered:
                    print(f"  ₹{exp[2]} - {exp[3]} on {exp[0]}")
            else:
                print("❌ No expenses found in this category.")

        elif choice == '5':
            confirm = input("Are you sure you want to reset this month's data? (y/n): ")
            if confirm.lower() == 'y':
                tracker.reset_month()

        elif choice == '6':
            print("👋 Thank you for using Expense Tracker. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
