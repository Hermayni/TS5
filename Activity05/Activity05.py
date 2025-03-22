import sys

def divide(num1, num2):
    if num2 == 0:
        return print("You can't divide by zero")
    else:
        return num1 / num2
    
def exponentiation(num1, num2):
    if num2 == 0:
        return 1
    else:
        return num1 ** num2
    
def remainder(num1, num2):
    if num2 == 0:
        return print("Error.You can't divide by zero")
    else:
        return num1 % num2
    
def summation(num1, num2):
    if num2 <= num1:
        return print("Error. The second number must be greater than the first number")
    else:
        return sum(range(num1, num2+1))

def menu():
    print("Math Operations Simulator")
    print("Please choose an operation")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")    
    print("[F] - Summation")
    print("[Q] - Quit")
    
    choice = input("Enter your choice: ").strip().upper()
    
    while choice != 'Q':
        if choice == 'D':
            try:
                num1 = float(input("Enter the numerator: "))
                num2 = float(input("Enter the denominator: "))
                result = divide(num1,num2)
                print("Result: ", result)
            except ValueError:
                print("Error. Please enter a valid number")
        elif choice == 'E':
            try:
                num1 = float(input("Enter the base number: "))
                num2 = float(input("Enter the exponent number: "))
                result = exponentiation(num1,num2)
                print("Result: ", result)
            except ValueError:
                print("Error. Please enter a valid number")
        elif choice == 'R':
            try:
                num1 = float(input("Enter the numerator: "))
                num2 = float(input("Enter the denominator: "))
                result = remainder(num1,num2)
                print("Result: ", result)
            except ValueError:
                print("Error. Please enter a valid number")
        elif choice == 'F':
            try:
                num1 = int(input("Enter the lower limit: "))
                num2 = int(input("Enter the upper limit: ")) 
                result = summation(num1,num2)
                print("Result: ", result)
            except ValueError:
                print("Error. Please enter a valid number")
        else: 
            print("Invalid choice. Please try again")
        print()
        menu()

        
    print("Thank you for using the Math Operations Simulator. Goodbye!")
    sys.exit()
                     
if __name__ == "__main__":
    menu()
