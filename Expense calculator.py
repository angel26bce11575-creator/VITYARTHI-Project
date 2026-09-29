FILE_NAME = "expenses_data.txt"
CATEGORIES = ("Food", "Transport", "Shopping", "Bills", "Entertainment",
              "Health", "Education", "Other")
PAYMENTS = ("Cash", "UPI", "Card", "Bank Transfer")

def line():
    print("-" * 78)

def heading(title):
    line()
    print(title.center(78))
    line()

def clean(text):
    return text.replace("|", "/").replace("\n", " ").strip()

def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for row in file:
                parts = row.strip().split("|")
                if len(parts) != 5:
                    continue
                date, category, description, amount, payment = parts
                try:
                    amount = float(amount)
                except ValueError:
                    continue
                expenses.append({"date": date, "category": category,
                                 "description": description, "amount": amount,
                                 "payment": payment})
    except FileNotFoundError:
        pass
    except PermissionError:
        print("\nWarning: expenses_data.txt cannot be read in this environment.")
        print("The program will start with an empty expense list.")
    return expenses

def save_expenses(expenses):
    """
    Save expenses to the data file.
    If the current environment is read-only, do not crash the program.
    """
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for e in expenses:
                row = "|".join([clean(e["date"]), clean(e["category"]),
                                clean(e["description"]), str(e["amount"]),
                                clean(e["payment"])])
                file.write(row + "\n")
        return True
    except PermissionError:
        print("\nWarning: This environment does not allow writing to expenses_data.txt.")
        print("Your expense is kept for this session, but it cannot be saved")
        print("after the program closes. Run the program in a writable folder")
        print("such as a normal local Python/VS Code project folder.")
        return False
    except OSError as error:
        print(f"\nWarning: Could not save the data file: {error}")
        return False

def get_amount():
    while True:
        value = input("Enter amount: ").strip()
        try:
            amount = float(value)
            if amount > 0:
                return amount
            print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

def choose_from(items, title):
    print(f"\n{title}:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    while True:
        choice = input("Enter choice number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(items):
            return items[int(choice) - 1]
        print("Invalid choice. Try again.")

def add_expense(expenses):
    heading("ADD EXPENSE")
    expense = {
        "date": clean(input("Enter date (DD-MM-YYYY): ")),
        "category": choose_from(CATEGORIES, "Categories"),
        "description": clean(input("Enter description: ")),
        "amount": get_amount(),
        "payment": choose_from(PAYMENTS, "Payment Methods")
    }
    expenses.append(expense)
    if save_expenses(expenses):
        print("Expense added and saved successfully.")
    else:
        print("Expense added successfully for this session.")

def show_expense(number, e):
    print(f"{number:<4}{e['date']:<14}{e['category']:<16}"
          f"{e['description']:<24}₹{e['amount']:>9.2f}  {e['payment']}")

def view_expenses(expenses):
    heading("ALL EXPENSES")
    if not expenses:
        print("No expenses recorded.")
        return
    print(f"{'No.':<4}{'Date':<14}{'Category':<16}"
          f"{'Description':<24}{'Amount':>10}  Payment")
    line()
    for i, e in enumerate(expenses, 1):
        show_expense(i, e)
    line()
    print(f"Total expenses: ₹{sum(e['amount'] for e in expenses):.2f}")

def search_expenses(expenses):
    heading("SEARCH EXPENSES")
    if not expenses:
        print("No expenses available.")
        return
    keyword = input("Enter keyword: ").strip().lower()
    matches = []
    for e in expenses:
        text = f"{e['description']} {e['category']} {e['payment']}".lower()
        if keyword in text:
            matches.append(e)
    if not matches:
        print("No matching expenses found.")
        return
    for i, e in enumerate(matches, 1):
        show_expense(i, e)

def category_summary(expenses):
    heading("CATEGORY SUMMARY")
    if not expenses:
        print("No expenses available.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    total = sum(totals.values())
    print(f"{'Category':<20}{'Amount':>15}{'Share':>12}")
    line()
    for category, amount in sorted(totals.items()):
        print(f"{category:<20}₹{amount:>13.2f}{amount/total*100:>10.2f}%")
    line()
    print(f"{'Grand Total':<20}₹{total:>13.2f}")

def payment_summary(expenses):
    heading("PAYMENT METHOD SUMMARY")
    if not expenses:
        print("No expenses available.")
        return
    totals = {}
    for e in expenses:
        totals[e["payment"]] = totals.get(e["payment"], 0) + e["amount"]
    for method, amount in sorted(totals.items()):
        print(f"{method:<25}₹{amount:>13.2f}")

def monthly_summary(expenses):
    heading("MONTHLY SUMMARY")
    if not expenses:
        print("No expenses available.")
        return
    totals = {}
    for e in expenses:
        parts = e["date"].split("-")
        key = f"{parts[1]}-{parts[2]}" if len(parts) == 3 else "Unknown"
        totals[key] = totals.get(key, 0) + e["amount"]
    for month, amount in sorted(totals.items()):
        print(f"{month:<20}₹{amount:>15.2f}")

def highest_expense(expenses):
    heading("HIGHEST EXPENSE")
    if not expenses:
        print("No expenses available.")
        return
    e = max(expenses, key=lambda item: item["amount"])
    print(f"Date        : {e['date']}")
    print(f"Category    : {e['category']}")
    print(f"Description : {e['description']}")
    print(f"Amount      : ₹{e['amount']:.2f}")
    print(f"Payment     : {e['payment']}")

def delete_expense(expenses):
    heading("DELETE EXPENSE")
    if not expenses:
        print("No expenses available.")
        return
    view_expenses(expenses)
    while True:
        choice = input("Enter expense number (0 to cancel): ").strip()
        if choice == "0":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(expenses):
            removed = expenses.pop(int(choice) - 1)
            if save_expenses(expenses):
                print(f"Deleted {removed['description']} successfully.")
            else:
                print(f"Deleted {removed['description']} for this session.")
            return
        print("Invalid expense number.")

def budget_check(expenses):
    heading("BUDGET CHECK")
    if not expenses:
        print("No expenses available.")
        return
    budget = get_amount()
    spent = sum(e["amount"] for e in expenses)
    remaining = budget - spent
    print(f"Budget : ₹{budget:.2f}")
    print(f"Spent  : ₹{spent:.2f}")
    if remaining >= 0:
        print(f"Remaining: ₹{remaining:.2f}")
        print("You are within the entered budget.")
    else:
        print(f"Over budget by: ₹{abs(remaining):.2f}")

def dashboard(expenses):
    heading("EXPENSE DASHBOARD")
    count = len(expenses)
    total = sum(e["amount"] for e in expenses)
    average = total / count if count else 0
    highest = max((e["amount"] for e in expenses), default=0)
    categories = {e["category"] for e in expenses}
    print(f"Number of expenses : {count}")
    print(f"Total spending     : ₹{total:.2f}")
    print(f"Average expense    : ₹{average:.2f}")
    print(f"Highest expense    : ₹{highest:.2f}")
    print(f"Categories used    : {len(categories)}")

def show_menu():
    heading("PERSONAL EXPENSE TRACKER")
    menu = ("Add Expense", "View All Expenses", "Search Expenses",
            "Category Summary", "Payment Summary", "Monthly Summary",
            "Highest Expense", "Budget Check", "Dashboard",
            "Delete Expense", "Exit")
    for i, item in enumerate(menu, 1):
        print(f"{i:>2}. {item}")
    line()

def main():
    expenses = load_expenses()
    print("\nWelcome to Personal Expense Tracker!")
    print(f"{len(expenses)} saved expense(s) loaded.")
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            search_expenses(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            payment_summary(expenses)
        elif choice == "6":
            monthly_summary(expenses)
        elif choice == "7":
            highest_expense(expenses)
        elif choice == "8":
            budget_check(expenses)
        elif choice == "9":
            dashboard(expenses)
        elif choice == "10":
            delete_expense(expenses)
        elif choice == "11":
            save_expenses(expenses)
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select a menu number.")

if __name__ == "__main__":
    main()
