#compute the operator list menu
def bitwise_operations(a, b) :

    print(f"a = {a}, b = {b}")
    print(f"a & b = {a & b}")  # Bitwise AND
    print(f"a | b = {a | b}")  # Bitwise OR
    print(f"a ^ b = {a ^ b}")  # Bitwise XOR
    print(f"~a = {~a}")        # Bitwise NOT
    print(f"~b = {~b}")        # Bitwise NOT
    print(f"a << 2 = {a << 2}") # Left Shift
    print(f"a >> 2 = {a >> 2}") # Right Shift


 def arithmetic_operations(a, b) :

    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")   # Addition
    print(f"a - b = {a - b}")   # Subtraction
    print(f"a * b = {a * b}")   # Multiplication
    print(f"a / b = {a / b}")   # Division
    print(f"a // b = {a // b}") # Floor Division
    print(f"a % b = {a % b}")   # Modulus
    print(f"a ** b = {a ** b}") # Exponentiation


def logical_operations(a, b) :

    print(f"a = {a}, b = {b}")
    
    # AND operator
    print(f"a and b = {a and b}")  # True if both are true

    # OR operator
    print(f"a or b = {a or b}")    # True if at least one is true

    # NOT operator
    print(f"not a = {not a}")       # True if a is false
    print(f"not b = {not b}")       # True if b is false


def menu() :

    print("Menu:")
    print("1. Bitwise_operations")
    print("2. arithmetic_operations")
    print("3. logical_operations")
    print("4. Exit")

while True :

    menu()
    choice = input("Select an option (1-4): ")

    if choice in ['1', '2', '3'] :

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

    if choice == '1' :

        print(f"Result: {bitwise_operations(a, b)}")

    elif choice == '2' :

        print(f"Result: {arithmetic_operations(a, b)}") 

    elif choice == '3' :

        print(f"Result: {logical_operations(a, b)}")

    elif choice == '4' :

        print("Exiting the program.")
        break

    else :

        print("Invalid choice! Please select a valid option.")
