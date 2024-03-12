# Simple functional Calculator ( * - + / )

def my_sum(a,b):
    result = a+b
    print(f"a + b = {result}")

def my_sub(a,b):
    result = a-b
    print(f"a - b = {result}")

def my_mul(a,b):
    result = a*b
    print(f"a * b = {result}")

def my_div(a,b):
    result = a/b
    print(f"a / b = {result}")

def Calculate():
    
    a = int(input("enter the first number\n"))
    b = int(input("enter the second operator\n"))
    op = input("enter a simple operator \n")

    match op:
     case "+":
        my_sum(a,b)
     case "-":
        my_sub(a,b)
     case "*":
        my_mul(a,b)
     case "/":
        my_div(a,b)
     case _:
        print("incorrect Operator!!")
         
          
Calculate()
