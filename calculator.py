def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", addition(num1, num2))
elif choice == '2':
    print("Result:", subtraction(num1, num2))
elif choice == '3':
    print("Result:", multiplication(num1, num2))
elif choice == '4':
    print("Result:", division(num1, num2))
else:
    print("Invalid input")