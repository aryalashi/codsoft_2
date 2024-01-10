# Function to add two numbers
def add(x, y):
    return x + y
# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Function to perform calculations
def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4/5): ")
        if choice in ('1', '2', '3', '4','5'):
            break
        else:
            print("Invalid input, please enter again.")

    num1 = float(input("Enter first number: "))#get 1st input
    num2 = float(input("Enter second number: "))#get 2nd input

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)


    print(f"Result is: {result}")
calculate()