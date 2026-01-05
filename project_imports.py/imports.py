import sys
import importlib

# PART 1: Simulated "Module"

class MathUtils:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


math_utils = MathUtils()


# PART 2: Behind the scenes of import

def explain_import_process():
    print("\n HOW IMPORT WORKS (Behind the Scenes)\n")

    print("Python checks module cache (sys.modules)")
    print("Is 'math' already loaded? ->", "math" in sys.modules)

    print("\n Python checks search paths (sys.path)")
    for path in sys.path[:5]:   # first 5 paths only
        print("  ", path)

    print("\n If found, Python compiles to bytecode (__pycache__)")
    print("Module code executes ONCE")
    print("Module object is stored in sys.modules\n")



# PART 3: Real import example

def real_import_demo():
    print("Importing built-in module: math")

    import math
    print("Square root of 16 =", math.sqrt(16))

    print("\nImporting SAME module again...")
    import math
    print("Math module reloaded? No (cached in sys.modules)")



# PART 4: __name__ behavior

def name_demo():
    print("\n __name__ behavior")
    print("__name__ value is:", __name__)

    if __name__ == "__main__":
        print("This file is running directly")
    else:
        print("This file is imported")


# PART 5: Main entry point

def main():
    print("MODULES & PACKAGES\n")

    # Using simulated module
    print("Using MathUtils (simulated module)")
    print("Add:", math_utils.add(10, 5))
    print("Sub:", math_utils.sub(10, 5))

    explain_import_process()
    real_import_demo()
    name_demo()

# ENTRY POINT PROTECTION

if __name__ == "__main__":
    main()
