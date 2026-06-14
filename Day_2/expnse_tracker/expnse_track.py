import json
import time

def log_call(func):
    def wrapper(*args, **kwargs):

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a") as log:
            log.write(
                f"{timestamp} | {func.__name__} | args={args} kwargs={kwargs}\n"
            )

        return func(*args, **kwargs)

    return wrapper

def load_expenses():
    try:
        with open("expense.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open("expense.json", "w") as file:
        json.dump(expenses, file, indent=2)


@log_call
def add_expense(category, amount):

    expenses = load_expenses()

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully!")


@log_call
def get_summary():

    expenses = load_expenses()

    summary = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    return summary


@log_call
def view_all():

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\nAll Expenses")
    print("----------------")

    for expense in expenses:
        print("Category:", expense["category"])
        print("Amount:", expense["amount"])
        print("-----------------")


def read_logs():

    try:
        add_count = 0
        summary_count = 0
        view_count = 0
        with open("log.txt", "r") as file:

            for line in file:

                if "add_expense" in line:
                    add_count += 1

                elif "get_summary" in line:
                    summary_count += 1

                elif "view_all" in line:
                    view_count += 1

        print("add_expense :", add_count)
        print("get_summary :", summary_count)
        print("view_all :", view_count)

    except FileNotFoundError:
        print("No logs found.")
   
while True:

    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Summary")
    print("3. View All")
    print("4. Read Logs")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        category = input("Enter category: ")

        try:
            amount = float(input("Enter amount: "))
            add_expense(category, amount)

        except ValueError:
            print("Invalid amount!")

    elif choice == "2":

        summary = get_summary()

        if not summary:
            print("No expenses found.")

        else:
            print("\nExpense Summary")
            print("-" * 30)

            for category in summary:
                print(category, ":", summary[category])

    elif choice == "3":

        view_all()

    elif choice == "4":

        read_logs()

    elif choice == "5":

        print("Goodbye!")
        break

    else:
        print("Invalid choice!")