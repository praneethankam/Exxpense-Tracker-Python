import sqlite3
from datetime import datetime

# Initialize database
def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, description, amount) VALUES (?, ?, ?)", (date, description, amount))
    conn.commit()
    conn.close()
    print("Expense added successfully!")

# View all expenses with Serial IDs
def view_summary():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, SUM(amount) FROM expenses GROUP BY description")
    data = cursor.fetchall()
    
    total = sum(row[2] for row in data)
    print(f"\nTotal Expenses: {total}")
    print("Category-wise Breakdown:")
    for row in data:
        print(f" {row[0]}, description: {row[1]}, Total: {row[2]}")
    
    conn.close()

# Search expenses by date, showing Serial IDs
def search_by_date():
    date = input("Enter the date (YYYY-MM-DD): ")
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, description, amount FROM expenses WHERE date = ?", (date,))
    data = cursor.fetchall()
    
    if data:
        print(f"\nExpenses on {date}:")
        for row in data:
            print(f"ID: {row[0]}, description: {row[2]}, Amount: {row[3]}")
    else:
        print("No expenses found for this date.")
    
    conn.close()

#delte record    
def delete_record():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    # Fetch all records and display them
    cursor.execute("SELECT id, date, description, amount FROM expenses")
    data = cursor.fetchall()

    # Check if there are any records
    if not data:
        print("No records found in the database.")
        conn.close()
        return

    # Print all the records
    print("\nRecords in the database:")
    for row in data:
        print(f"ID: {row[0]}, Date: {row[1]}, description: {row[2]}, Amount: {row[3]}")

    # Ask the user to enter the ID of the record they want to delete
    try:
        record_id = int(input("\nEnter the ID of the record you want to delete: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer for the record ID.")
        conn.close()
        return

    # Check if the record with the provided ID exists
    cursor.execute("SELECT id FROM expenses WHERE id = ?", (record_id,))
    data = cursor.fetchone()

    if data:  # If record exists, delete it
        cursor.execute("DELETE FROM expenses WHERE id = ?", (record_id,))
        conn.commit()
        print(f"Record with ID {record_id} deleted successfully!")
    else:  # If no record found with that ID
        print(f"No record found with ID {record_id}.")
    
    conn.close()

# Main menu
def main():
    init_db()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Search by Date")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            search_by_date()
        elif choice == "4":
            delete_record()    
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
