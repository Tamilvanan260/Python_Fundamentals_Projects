import traceback
# Function 1: Divide Numbers Safely

def divide_numbers():
    print("\n--- Divide Numbers Safely ---")
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Invalid input, please enter numbers only.")
    else:
        print("Result:", result)
    finally:
        print("Operation finished.\n")



# Function 2: File Operations

def file_operations():
    print("\n--- File Operations ---")
    try:
        with open("users.txt", "r") as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("File not found! Creating 'users.txt'...")
        with open("users.txt", "w") as file:
            file.write("User log start\n")
        print("'users.txt' created successfully.")
    finally:
        print("File operation completed.\n")



# Function 3: Input Validation

def input_validation():
    print("\n--- Input Validation ---")
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative!")
            break  # exit loop if input is valid
        except ValueError as ve:
            print("Error:", ve)
    print("Valid age entered:", age, "\n")



# Function 4: Error Logging System

def error_logging():
    print("\n--- Error Logging System ---")
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        result = x / y
    except Exception as e:
        print("An error occurred! Check 'error_log.txt'.")
        with open("error_log.txt", "a") as log_file:
            log_file.write(traceback.format_exc())
            log_file.write("\n\n")
    else:
        print("Division Result:", result)
    finally:
        print("Error logging operation finished.\n")


# Function 5: Custom Exception Example

class NegativeNumberError(Exception):
    """Custom Exception for negative numbers"""
    pass

def custom_exception_demo():
    print("\n--- Custom Exception Demo ---")
    try:
        num = int(input("Enter a positive number: "))
        if num < 0:
            raise NegativeNumberError("You entered a negative number!")
    except NegativeNumberError as ne:
        print("Custom Error:", ne)
    except ValueError:
        print("Please enter a valid integer!")
    else:
        print("You entered:", num)
    finally:
        print("Custom exception demo finished.\n")


# Main Program Menu

def main():
    while True:
        print("\n==== Exception Handling Project ====")
        print("1. Divide Numbers Safely")
        print("2. File Operations")
        print("3. Input Validation")
        print("4. Error Logging System")
        print("5. Custom Exception Demo")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            divide_numbers()
        elif choice == '2':
            file_operations()
        elif choice == '3':
            input_validation()
        elif choice == '4':
            error_logging()
        elif choice == '5':
            custom_exception_demo()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number between 1-6.")


# Run the program

if __name__ == "__main__":
    main()
