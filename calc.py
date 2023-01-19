def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2    

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def calculator():
    num1 = float(input('enter first number : '))
    while True:
        num2 = float(input('enter next number -note(number should not be zero) : '))
        operations = {'+':add(num1,num2),'-':sub(num1,num2),'*':multiply(num1,num2),'/':divide(num1,num2)}
        ops = operations[input('enter the operation : ')]
        result = ops
        print(f'the result is {result}')

        new_cal = input(f'do you want to continue with the {result} type "y" else type "n" : ')


        if new_cal == 'y':
            num1 = result
            continue
        else:
            calculator()    

calculator()