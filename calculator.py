def calculator():
    history = []

    def adda(a,b):
        result = a+b
        history.append(f"{a}+{b} = {result}")
        return result

    def subtract(a,b):
        result = a-b
        history.append(f"{a}-{b}={result}")
        return result

    def multiply(a,b):
        result= a*b
        history.append(f"{a}*{b}={result}")
        return result
    def divide(a,b):
        if b==0:
            return"Error! Division by zero!"
        result =a/b
        history.append(f"{a}/{b}={result}")
        return result
    def print_history():
        print("\nHistory:")
        for entry in history:
            print(entry)
        print()

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6.Exit")

        choice = input("Enter choice (1/2/3/4/5/6):")
        if choice in ('1','2','3','4'):
            num1 = float(input("Enter first number:"))
            num2 =  float(input("Enter second number:"))
            if choice =='1':
                print("Result:",add(num1,num2))
            elif choice =='2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice =='4':
                print("Result:", divide(num1, num2))
            elif choice =='5':
                print_history()
            elif choice =='6':
                print("Exiting calculator. Goodbye!")
                break
            else:
                print("Invalid Input")
        calculator()