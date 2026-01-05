class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
        else:
            self.balance += amount
            print(f"₹{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than zero")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# -------- MAIN PROGRAM --------

name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n--- MINI BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("👋 Thank you for using Mini Bank App")
        break

    else:
        print("⚠ Invalid choice, please try again")
