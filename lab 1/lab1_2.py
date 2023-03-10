def summtion (num1,num2) :
    return num1+num2
def subtraction (num1,num2) :
    return num1-num2
def multiplication (num1,num2):
    return num1*num2
def division (num1,num2):
    return num1 / num2

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
if isinstance(num1,int) and isinstance(num2,int):
    print(f'num1 + num2 = {summtion(num1,num2)}')
    print(f'num1 - num2 = {subtraction(num1,num2)}')
    print(f'num1 * num2 = {multiplication(num1,num2)}')
    print(f'num1 / num2 = {division(num1,num2)}')
