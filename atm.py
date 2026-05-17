# Simple ATM without deposit

balance = 20000  # Starting balance
correct_pin = 3796

print("\nWelcome to the ATM")
user_pin = int(input("Please enter your 4 digit pin: "))

if user_pin == correct_pin:    
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        print(f"Your balance is: Rs. {balance}")
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print(f"Please collect your cash: Rs. {amount}")
            print(f"Updated balance: Rs. {balance}")
        else:
            print("Error: Insufficient balance!")
    elif choice == 3:
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid choice selected. Please try again.")
else:
    print("Invalid PIN")