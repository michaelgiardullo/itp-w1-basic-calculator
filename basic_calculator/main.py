"""This is the entry point of the program."""


def basic_calculator(num1,num2,operation):
    
    if isinstance(num1,str) == True or isinstance(num2,str) == True:
        return "Invalid Inputs"
    
    if operation == 'add':
        return num1+num2
    elif operation == 'subtract':
        return num1-num2
    elif operation == 'multiply':
        return num1*num2
    elif operation == 'divide':
        return num1/num2
    else:
        return "Invalid operation"
