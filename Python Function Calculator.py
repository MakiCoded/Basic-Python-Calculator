def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def division(a,b):
    return a/b
def multiplication(a,b):
    return a*b


mathOperations = {"+":add, "-":subtraction, "/":division, "*":multiplication}

def Calculator():
    num1 = int(input("Enter First Number: "))
 
    print("These are the Available Math Operation")
    for operation in mathOperations.keys():
        print(operation)
    
    should_continue = True
    while should_continue:
        userSelection = (input("Pick and Operation or type stop to exit : \n"))
        if userSelection == "stop":
            break

        if userSelection not in mathOperations:
            print("invalid operator! try again")
            continue

        num2 = int(input("Enter Second Number: "))

        calculation_funtion = mathOperations[userSelection]

        answer = calculation_funtion(num1, num2)

        print(f"{num1}{userSelection}{num2} = {answer}")
    
        nextStep =input(F"Would you like to continue with {answer}? (Yes/no):").lower()
        if nextStep == "yes":
            num1 = answer
        else: 
            should_continue = False
            Calculator()

Calculator()
        


