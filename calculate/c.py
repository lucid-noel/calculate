a = float(input("number1: "))
b = float(input("number2: "))
op = input("choose (+,-,*,/,**): ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "**":
    result = a ** b    
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("0 is not divisible")
        exit()
        result = a / b        
else:
    print("wrong")
    exit()

print("answer:" , result)   