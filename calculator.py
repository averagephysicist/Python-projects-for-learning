print("Welcome to the super basic calculator!")

n1 = float(input("Type in the first number: \n"))
n2 = float(input("Type in the second number: \n "))


def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2

opertations = {
    "+": add,
    "-": subtract,
    "/": divide, 
    "*": multiply
}

operation = input("Type in the operation you want to perform: +, -, /, * ")

if operation in opertations:
    result = opertations[operation](n1, n2)
    print(f"result: {result}")
else:
    print("invalid operation")    