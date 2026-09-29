# Personal Expense Tracker

## Project Overview

**Personal Expense Tracker** is a beginner-friendly, menu-driven Python console application
that allows a user to record, view, search, analyze, budget, and delete personal expenses.

The project is built using fundamental Python concepts such as:

- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Functions
- Loops
- Conditional statements
- Exception handling
- File handling

No external Python packages or database software are required.

---

## 1. Project Features

The application provides the following features:

1. **Add Expense** – Record a new expense with date, category, description, amount, and payment method.
2. **View All Expenses** – Display all stored expenses and the total spending.
3. **Search Expenses** – Search expenses using a keyword from the description, category, or payment method.
4. **Category Summary** – Calculate total spending and percentage share for each category.
5. **Payment Summary** – Calculate total spending for each payment method.
6. **Monthly Summary** – Display spending grouped by month and year.
7. **Highest Expense** – Find and display the largest individual expense.
8. **Budget Check** – Compare total recorded spending with a user-entered budget.
9. **Dashboard** – Display the number of expenses, total spending, average expense, highest expense, and number of categories used.
10. **Delete Expense** – Remove a selected expense from the records.
11. **Exit** – Save the current data and close the application.

---

## 2. Prerequisites

Before running the project, make sure the following software is installed:

### Python

Python **3.x** is required.

Check whether Python is installed by opening a terminal or command prompt and running:

```bash
python --version
```

If that command does not work, try:

```bash
python3 --version
```

A version such as the following is acceptable:

```text
Python 3.10.x
Python 3.11.x
Python 3.12.x
Python 3.13.x
```

No additional Python libraries are required.

---

## 3. Project Structure

After downloading or extracting the project, the folder should contain:

```text
personal_expense_tracker/
│
├── expense_tracker.py
├── expenses.txt
├── README.md
└── Project_Report.docx
```

### File Description

| File | Purpose |
|---|---|
| `expense_tracker.py` | Main Python application |
| `expenses.txt` | Stores expense records |
| `README.md` | Project documentation and setup instructions |
| `Project_Report.docx` | Academic project report |

---

## 4. Environment Setup

### Step 1: Install Python

Download and install Python 3 from the official Python website if it is not already installed.

During Windows installation, enable the option:

```text
Add Python to PATH
```

This allows Python to be executed directly from Command Prompt or PowerShell.

### Step 2: Verify Installation

Open Command Prompt, PowerShell, Terminal, or another terminal application and run:

```bash
python --version
```

or:

```bash
python3 --version
```

If Python is installed correctly, its version number will be displayed.

### Step 3: Open the Project Folder

Navigate to the folder containing:

```text
expense_tracker.py
```

For example, on Windows:

```bash
cd path/to/personal_expense_tracker
```

On macOS/Linux:

```bash
cd /path/to/personal_expense_tracker
```

---

## 5. Dependency Installation

This project uses **only Python built-in functionality**.

Therefore, there are:

- No external packages
- No `pip install` commands
- No `requirements.txt` file
- No database installation
- No API keys
- No environment variables required

The project can be run directly after Python 3 is installed.

---

## 6. Configuration

The application does not require special configuration.

The data file is automatically expected at:

```text
expenses.txt
```

in the same directory as:

```text
expense_tracker.py
```

The program uses the following categories:

```text
Food
Transport
Shopping
Bills
Entertainment
Health
Education
Other
```

The available payment methods are:

```text
Cash
UPI
Card
Bank Transfer
```

The application creates or updates `expenses.txt` automatically when expenses are saved.

---

## 7. Running the Project

### Windows

Open Command Prompt or PowerShell in the project directory and run:

```bash
python expense_tracker.py
```

### macOS/Linux

Run:

```bash
python3 expense_tracker.py
```

If the Python command is configured as `python`, you can also use:

```bash
python expense_tracker.py
```

---

## 8. First Run

When the program starts, it loads the existing records from:

```text
expenses.txt
```

You will see a menu similar to:

```text
------------------------------------------------------------------------------
                         PERSONAL EXPENSE TRACKER
------------------------------------------------------------------------------

 1. Add Expense
 2. View All Expenses
 3. Search Expenses
 4. Category Summary
 5. Payment Summary
 6. Monthly Summary
 7. Highest Expense
 8. Budget Check
 9. Dashboard
10. Delete Expense
11. Exit
------------------------------------------------------------------------------
```

Enter the number of the operation you want to perform.

---

## 9. Adding an Expense

Select:

```text
1. Add Expense
```

The program asks for:

```text
Enter date (DD-MM-YYYY):
```

Then select a category, enter a description, enter the amount, and select a payment method.

For example:

```text
Enter date (DD-MM-YYYY): 29-09-2026

Categories:
1. Food
2. Transport
3. Shopping
4. Bills
5. Entertainment
6. Health
7. Education
8. Other

Enter choice number: 1

Enter description: Lunch
Enter amount: 150

Payment Methods:
1. Cash
2. UPI
3. Card
4. Bank Transfer

Enter choice number: 2
```

The expense will be added to the list and saved to `expenses.txt`.

---

## 10. Viewing Expenses

Select:

```text
2. View All Expenses
```

The program displays the saved records in a table and calculates the total expense.

Example:

```text
No. Date          Category        Description                 Amount  Payment
1   25-09-2026    Food            Lunch                       ₹150.00  UPI
2   25-09-2026    Transport       Bus ticket                   ₹40.00  Cash
```

---

## 11. Searching Expenses

Select:

```text
3. Search Expenses
```

Enter a keyword such as:

```text
food
```

or:

```text
lunch
```

or:

```text
upi
```

The application performs a case-insensitive search through the description,
category, and payment method.

---

## 12. Viewing Summaries

### Category Summary

Select:

```text
4. Category Summary
```

This calculates spending for each category and displays its percentage share.

### Payment Summary

Select:

```text
5. Payment Summary
```

This calculates how much has been spent using each payment method.

### Monthly Summary

Select:

```text
6. Monthly Summary
```

This groups expenses according to the month and year entered in the date field.

---

## 13. Budget Check

Select:

```text
8. Budget Check
```

Enter a positive budget amount.

The program compares the entered budget with the total of the currently stored expenses.

If spending is below the budget, the remaining amount is displayed.

If spending is above the budget, the amount exceeded is displayed.

---

## 14. Dashboard

Select:

```text
9. Dashboard
```

The dashboard displays:

```text
Number of expenses
Total spending
Average expense
Highest expense
Categories used
```

This provides a quick overview of the stored expense data.

---

## 15. Deleting an Expense

Select:

```text
10. Delete Expense
```

The application displays the current expenses and asks for the number of the
record to remove.

For example:

```text
Enter expense number (0 to cancel): 2
```

The selected record is removed and the updated data is saved.

Enter:

```text
0
```

to cancel the operation.

---

## 16. Data Storage Format

The application stores records in a plain text file called:

```text
expenses.txt
```

Each record follows this format:

```text
date|category|description|amount|payment_method
```

Example:

```text
25-09-2026|Food|Lunch|150.0|UPI
```

The pipe character (`|`) separates the fields.

The application automatically loads these records when it starts.

---

## 17. Python Concepts Demonstrated

### Strings

Used for:

- Dates
- Descriptions
- Categories
- Payment methods
- User input
- Searching

### Lists

The main expense collection is a list containing multiple dictionaries.

### Tuples

Fixed categories and payment methods are stored as tuples.

Example:

```python
CATEGORIES = (
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Health",
    "Education",
    "Other"
)
```

### Dictionaries

Each expense is represented by a dictionary:

```python
{
    "date": "25-09-2026",
    "category": "Food",
    "description": "Lunch",
    "amount": 150.0,
    "payment": "UPI"
}
```

### Sets

Sets are used to identify unique expense categories for the dashboard.

### Functions

Different tasks are separated into functions such as:

```text
add_expense()
view_expenses()
search_expenses()
category_summary()
payment_summary()
monthly_summary()
highest_expense()
budget_check()
dashboard()
delete_expense()
```

### Loops

Loops are used for:

- Menu processing
- Displaying records
- Validating input
- Calculating summaries

### Conditional Statements

`if`, `elif`, and `else` statements control the menu and validation logic.

### Exception Handling

`try` and `except` are used to handle invalid numeric input and missing files.

### File Handling

Python's `open()` function is used to read and write `expenses.txt`.

---

## 18. Error Handling

The program handles several common errors.

### Invalid Amount

If the user enters:

```text
abc
```

instead of a number, the program displays an error and asks again.

### Zero or Negative Amount

The application does not accept:

```text
0
```

or negative values.

### Invalid Menu Choice

If an invalid menu number is entered, the application displays an error and
returns to the menu.

### Missing Data File

If `expenses.txt` does not exist, the application starts with an empty expense list.
The file will be created when data is saved.

---

## 19. Troubleshooting

### Problem: `python` is not recognized

Try:

```bash
python3 --version
```

If Python is not installed, install Python 3 and make sure it is added to PATH.

### Problem: File Not Found

Make sure the terminal is opened in the same directory as:

```text
expense_tracker.py
```

Then run:

```bash
python expense_tracker.py
```

### Problem: Expenses are not appearing

Check that:

```text
expenses.txt
```

is located in the same folder as:

```text
expense_tracker.py
```

Also make sure the program has permission to read and write files in the directory.

### Problem: Data format looks incorrect

Do not manually remove or change the `|` separators in `expenses.txt`.

Each record should contain exactly five fields:

```text
date|category|description|amount|payment
```

---

## 20. Stopping the Application

To safely close the program, select:

```text
11. Exit
```

The program saves the current records before terminating.

Avoid closing the terminal while the program is in the middle of writing data.

---

## 21. Project Limitations

The current version is intentionally simple for learning purposes.

Limitations include:

- Console-based interface
- Plain text storage
- No login or authentication
- No database
- Basic date validation
- No multi-user support
- No graphical charts
- No automatic bank transaction import

---

## 22. Future Enhancements

Possible future improvements include:

1. Add a graphical user interface using Tkinter.
2. Replace the text file with an SQLite database.
3. Add user login and multiple user accounts.
4. Add income and savings tracking.
5. Add recurring expenses.
6. Add date-range filtering.
7. Add graphical spending charts.
8. Export reports to CSV or PDF.
9. Add stronger date validation.
10. Add financial goals and monthly budgets.

---

## 23. Academic Information

**Project Title:** Personal Expense Tracker  
**Student Name:** Angel Sabu  
**Project Type:** Python Fundamentals Project  
**Programming Language:** Python 3  
**Application Type:** Console Application  
**External Dependencies:** None  

---

## 24. Author

**Angel Sabu**

This project was created as an academic Python programming project to demonstrate
the practical use of fundamental Python programming concepts.

---

## 25. Quick Start

For an evaluator who wants to run the project immediately:

```bash
cd personal_expense_tracker
python expense_tracker.py
```

Then choose an option from the displayed menu.

No dependency installation or additional configuration is required.

