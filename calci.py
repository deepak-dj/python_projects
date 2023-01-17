import time
print('------------------------------------------------------')
print('============== WELCOME TO MY CALCI ===================')
print('------------------------------------------------------')

time.sleep(3)
print()
print('here you can perform mathmatical operations like addition,substraction,multiplication and division')
print()
time.sleep(3)


class calci():
    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return(self.num1+self.num2)
    def sub(self):
        return (self.num1-self.num2)    
    def multiply(self):
        return (self.num1*self.num2)
    def divide(self):
        return (self.num1/self.num2)  

class Overloading():
        def __init__(self,num) -> None:
            self.num = num

        def __add__(self,C):
            return(self.num+C.num)    
        def __sub__(self,C):
            return(self.num-C.num)
        def  __mul__(self,C):
            return(self.num*C.num)
        def __truediv__(self,C):
            return(self.num/C.num)    


while True:
    num1 = int(input('enter 1st number : '))
    num2 = int(input('enter 2nd number : '))
    operation = input('select operation\n+\n-\n*\n/\n------\n')
    c = calci(num1,num2)
    if operation == '+':
        new_num = c.add()
    elif operation == '-':
        new_num = c.sub()
    elif operation == '*':
        new_num = c.multiply()
    elif operation == '/':
        new_num = c.divide()
    else:
        print('plz choose the valid operation') 
    print()      
    print(f'the output is {int(new_num)}')  

    print()
    choice = input('type "y" if you want to continue with the reasultant value or for new inputs press "n", To close the claculator press x\n--------\n').lower()
    if choice == 'x':
        print()
        print('closing the calci ....')
        time.sleep(3)
        print("================= Thank You !!! =====================")
        break 
    while choice != 'n':
            c1 = Overloading(new_num)
            c2 = Overloading(int(input('enter 2nd number : ')))
            ops = input('select operation\n+\n-\n*\n/\n------\n')
            if ops == '+':
                new_num = c1+c2
            elif ops == '-':
                new_num = c1-c2
            elif ops == '*':
                new_num = c1*c2
            elif ops == '/':
                new_num = c1/c2
            else:
                print('plz choose the valid operation')
            print()    
            print(f'the output is {int(new_num)}')    
            print()  
            options = input('want to continue type "c" and want a fresh start press "s"\n------\n').lower()    
            if options != 'c':
                break
            
    


           
