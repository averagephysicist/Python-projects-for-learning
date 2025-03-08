while True:
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
        result = float(opertations[operation](n1, n2))
        print(f"{n1} {operation} {n2} = {result}")
    else:
        print("invalid operation")    

    use_result = input("Would you like to use your result to perform further calculations? Press \' y \' or \' n\'").lower()
    if use_result == "y":
        n1 = result
        n2 = float(input("Type in the second number: \n "))
        operation = input("Type in the operation you want to perform: +, -, /, * ")
        if operation in opertations:
            result = float(opertations[operation](n1, n2))
            print(f"{n1} {operation} {n2} = {result}")
        else:
            print("invalid operation")   


    else:
        continue
    

    choice = input("Press \' y \' to continue. Press \' n \' to exit." ).lower() 
    if choice == "y" :
        continue
    else:
        break