import csv
import logging

# ---------------- LOG FILE SETUP ----------------
logging.basicConfig(
    filename="logs/app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

CSV_FILE = "users_50.csv"

# ---------------- READ CSV ----------------
def read_users():
    try:
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            print("\n--- USERS LIST ---")
            for row in reader:
                print(row)

    except FileNotFoundError:
        logging.error("CSV file not found")
        print("CSV file not found")

    except Exception as e:
        logging.error(str(e))
        print("Error while reading CSV")


# ---------------- WRITE CSV ----------------
def add_user():
    try:
        user_id = input("Enter ID: ").strip()
        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        email = input("Enter Email: ").strip()

        # Read headers first
        with open(CSV_FILE, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames

        # Append new row using DictWriter
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow({
                'id': user_id,
                'name': name,
                'age': age,
                'email': email
            })

        print("User added successfully")

    except Exception as e:
        logging.error(str(e))
        print("Error while writing CSV")


# ---------------- ERROR EXAMPLE ----------------
def divide_numbers():
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        logging.error("Division by zero error")
        print("Cannot divide by zero")

    except ValueError:
        logging.error("Invalid number input")
        print("Enter valid numbers")

    except Exception as e:
        logging.error(str(e))
        print("Unexpected error")


# ---------------- MAIN MENU ----------------
while True:
    print("\n1. Read Users")
    print("2. Add User")
    print("3. Divide Numbers (Error Logging)")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        read_users()
    elif choice == "2":
        add_user()
    elif choice == "3":
        divide_numbers()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid option")
