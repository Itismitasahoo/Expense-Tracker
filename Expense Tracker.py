expensesList = []
print("Welcome to Expense Tracker : ")

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit from Expense Tracker")

    choice = int(input("Please Enter Your choice : "))

    # ADD expense
    if choice == 1:
        date = input("Enter the date of your expense : ")
        category = input("Enter the category of Expense (Food, Travel, Shopping, EMI, Other) : ")
        description = input("Enter a short description of your expense : ")
        amount = float(input("Enter the amount you spent : "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\nYour expense has been added SUCCESSFULLY!")

    # VIEW all expenses
    elif choice == 2:
        if len(expensesList) == 0:
            print("No Expenses Added")
        else:
            print("\n==== Your Expenses Are ====")
            for i, eachExpense in enumerate(expensesList, start=1):
                print(f"Expense {i} --> {eachExpense['date']}, {eachExpense['category']}, "
                    f"{eachExpense['description']}, Amount: {eachExpense['amount']}")
                print("---------------------------")

    # VIEW total expenses
    elif choice == 3:
        total = 0
        for eachExpense in expensesList:
            total += eachExpense["amount"]

        print(f"\nTOTAL EXPENSES = {total}")

    # EXIT
    elif choice == 4:
        print("THANK YOU !!")
        break

    else:
        print("\n INVALID CHOICE. Try again ....")

