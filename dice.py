expenses = {}

def add_expense(date, category, amount):
    if date not in expenses:
        expenses[date] = []
    expenses[date].append({"category": category, "amount": amount})
    print(f"Added {amount} to {category} on {date}.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for date in expenses:
        print(f"\nDate: {date}")
        for item in expenses[date]:
            print(f"  Category: {item['category']} | Amount: {item['amount']}")

def total_expenses():
    total = 0
    for daily_expenses in expenses.values():
        for item in daily_expenses:
            total += item['amount']
    print(f"\nTotal Expenses: {total}")

def main():
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., food, rent, travel): ")
            try:
                amount = float(input("Enter amount: "))
                add_expense(date, category, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Track every rupee, value every penny — smart spending starts with knowing where your money goes. \n Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()