
import math                                                                                                      
print("Hi,welcome to my calculator") 

print("+ : sum")
print("_ : sub")
print("* : mul")
print("/ : div")
print("sin")
print("log")
print("sqrt")
print("cos")
print("tan")
print("cot")
print("factorial") 
print("enter your choice")
op=input()

if op == "+" or op == "_" or op == "*" or op == "/":
    a = float(input("enter first number: "))
    b = float(input("enter second number: ")) 
else:
    a=float(input("enter first number"))

if op == "+":
    result = a + b 


elif op == "-":
    result = a - b 
    
elif op == "*":
     result = a * b 


elif op == "/":
    result = a / b 
    if b == 0:
        result = " cant divide by zero."
elif op == "sin":
    result = math.sin(a)
elif op == "log":
    result = math.log(a)
elif op == "cos":
    result = math.cos(a)
elif op == "factorial":
    result = math.factorial(a)
elif op == "tan":
    result = math.tan(a)
elif op == "sqrt":
    result = math.sqrt(a)
elif op == "cot":
    result = math.cot(a)


print(result) 

 