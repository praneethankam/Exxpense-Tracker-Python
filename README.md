Expense Tracker
A simple, command-line based expense tracking application built using Python and SQLite. This program allows users to manage their expenses efficiently by adding, viewing, searching, and deleting expense records.

FEATURES
Add Expenses: Record your daily expenses with date, category, and amount.
View Summary: Get a breakdown of total expenses by category and a grand total.
Search by Date: Retrieve expenses for a specific date.
Delete Records: Remove specific expense records using their unique IDs.
Persistent Storage: Uses SQLite to store data, ensuring expenses are saved between sessions.
REQUIREMENTS
Python 3.x
SQLite (bundled with Python)
USAGE
Clone this repository:
Copy code
"git clone <repository_url>"
"cd Expense-Tracker-Python"
Run the program:
"python expense_tracker.py"
Follow the on-screen menu to manage your expenses:

1 to add a new expense
2 to view expense summaries
3 to search expenses by date
4 to delete a record
5 to exit the program
Database Structure
Table: expenses
id: Unique identifier for each record.
date: Date of the expense (YYYY-MM-DD).
category: Category of the expense (e.g., food, travel).
amount: Amount of the expense.
FUTURE ENHANCEMENT
Add user authentication for multiple accounts.
Implement data export to CSV.
Develop a GUI version for better user experience.
