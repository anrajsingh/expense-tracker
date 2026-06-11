expenses = []

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Expense name: ")
        amount = float(input("Amount: ₹"))
        expenses.append((item, amount))
        print("Expense added successfully!")

    elif choice == "2":
        total = 0

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nYour Expenses:")
            for item, amount in expenses:
                print(f"{item} - ₹{amount}")
                total += amount

            print(f"\nTotal Expense: ₹{total}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")