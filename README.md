
# **Python Fundamental Projects**

## **Overview**

This repository contains **5 Python fundamental projects** that demonstrate key Python concepts in a practical and interview-friendly way. Each project focuses on a specific concept and provides clean, well-structured code for easy understanding.

Projects included:

1. **File Handling** – Read/write CSV and log files
2. **Exception Handling** – Learn why errors happen and how to handle them safely
3. **OOP in Python** – Class & object concepts using Car and Bank examples
4. **Modules & Packages** – Understand how imports work behind the scenes
5. **Virtual Environments** – Importance of `venv` with real project example

---

## **1️⃣ File Handling**

**Description:**
This project demonstrates reading from and writing to CSV files, managing log files, and storing structured data efficiently.

**Concepts Covered:**

* `open()`, `read()`, `write()` functions
* CSV file handling using `csv` module
* Logging using `logging` module
* File modes (`r`, `w`, `a`)

**Practical Usage:**

* Storing user data or application logs
* Reading data for analysis from CSV

**Example:**

```python
import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Email'])
    writer.writerow(['Varun', 28, 'varun1@gmail.com'])
```

---

## **2️⃣ Exception Handling**

**Description:**
Learn to handle errors safely without crashing the program.

**Concepts Covered:**

* `try`, `except`, `finally` blocks
* Catching specific exceptions (`ZeroDivisionError`, `FileNotFoundError`)
* Raising exceptions using `raise`
* Custom error messages

**Practical Usage:**

* Prevent program crashes during runtime errors
* Handle invalid user input gracefully

**Example:**

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
finally:
    print("Execution finished.")
```

---

## **3️⃣ OOP in Python (Car / Bank Example)**

**Description:**
This project demonstrates **Object-Oriented Programming** using practical examples like a Car or Bank system.

**Concepts Covered:**

* Classes & objects
* `__init__` constructor
* Methods & attributes
* Encapsulation & simple abstraction

**Practical Usage:**

* Model real-world objects in software
* Build scalable and maintainable code

**Example (Bank Account):**

```python
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

acc = BankAccount("Varun", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)  # Output: 1300
```

---

## **4️⃣ Modules & Packages**

**Description:**
Learn how to create Python modules and packages and how `import` works under the hood.

**Concepts Covered:**

* Creating reusable `.py` files as modules
* Importing modules (`import module`, `from module import func`)
* Understanding Python search paths (`sys.path`)
* Structuring projects with packages

**Practical Usage:**

* Organize code for larger projects
* Reuse functions across multiple projects

**Example:**

```
project/
│
├── mymodule/
│   ├── __init__.py
│   └── utils.py
│
└── main.py
```

```python
# main.py
from mymodule.utils import greet

greet("Varun")
```

---

## **5️⃣ Virtual Environments (venv)**

**Description:**
Understand why virtual environments are essential for project isolation and dependency management.

**Concepts Covered:**

* Creating virtual environments: `python -m venv env`
* Activating venv: `env\Scripts\activate` (Windows)
* Installing packages locally with `pip install`
* Keeping dependencies separate for each project

**Practical Usage:**

* Avoid version conflicts between projects
* Ensure consistent environment for deployment

**Example:**

```powershell
# Windows
python -m venv myenv
myenv\Scripts\activate
pip install requests
```

---

## **Installation & Usage**

1. **Clone the repository**

```bash
git clone https://github.com/Tamilvanan260/Python_Fundamentals_Projects.git
cd Python_Fundamentals_Projects
```

2. **(Optional) Create Virtual Environment**

```bash
python -m venv env
env\Scripts\activate   # Windows
pip install -r requirements.txt   # if any packages
```

3. **Run any project**

```bash
python FileHandlingProject.py
python ExceptionHandlingProject.py
python OOPProject.py
# etc.
```

---

## **Key Skills Demonstrated**

* Python file I/O and logging
* Safe exception handling
* Object-oriented programming
* Modular project structure
* Environment and dependency management

---

## **Author**

**Tamil Vanan** – Python enthusiast | Full-stack & Data Science learner
[GitHub](https://github.com/Tamilvanan260)

---