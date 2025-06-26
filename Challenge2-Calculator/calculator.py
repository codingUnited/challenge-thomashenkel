import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

print("Welcome to your calculator!")

num1 = input("Enter the first number: ")
op = input("Enter an operation (+, -, *, /): ")
num2 = input("Enter the second number: ")

# TODO: Convert numbers and perform the operation

def PerformOperation(number1, number2, operator):
    try:
        return ops[operator](int(number1), int(number2))
    except ValueError:
        print("You can only submit numbers!")
    except ZeroDivisionError:
        print("You can't divide by zero silly!")
    

def ChainedOperation(result):
    number1 = result
    print(f"Previous result was: {result}")
    operation = input("Enter an operation (+, -, *, /): ")
    number2 = input("Enter the second number: ")
    result2 = PerformOperation(number1, number2, operation)
    print(f"The result is: {result2}")
    check = input("Would you like to continue with your previous result? Y/N: ")
    if check.lower() == ("y"):
        ChainedOperation(result2)

def main():
    result = PerformOperation(num1, num2, op)
    print(f"The result is: {result}")
    check = input("Would you like to continue with your previous result? Y/N: ")
    if check.lower() == ("y"):
        ChainedOperation(result)

main()