import matplotlib.pyplot as plt
from datetime import datetime

def plot_expense_summary(summary_dict):
    if not summary_dict:
        print("⚠️ No expenses to show in the report.")
        return

    month_name = datetime.now().strftime('%B_%Y')

    categories = list(summary_dict.keys())
    amounts = list(summary_dict.values())

    # Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.title('Expense by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.tight_layout()
    bar_file = f'bar_chart_{month_name}.png'
    plt.savefig(bar_file)
    plt.close()

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Distribution')
    plt.tight_layout()
    pie_file = f'pie_chart_{month_name}.png'
    plt.savefig(pie_file)
    plt.close()

    print(f"✅ Visual reports saved as '{bar_file}' and '{pie_file}'")
