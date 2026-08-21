
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/,%,//,**): ")

result = None

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("\nError: Division by zero is not allowed!")
elif op == '%':
    if num2 != 0:
        result = num1 % num2
    else:
        print("\nError: Modulo by zero is not allowed!")
elif op == '//':
    if num2 != 0:
        result = num1 // num2
    else:
        print("\nError: Floor division by zero is not allowed!")
elif op == '**':
    result = num1 ** num2
else:
    print("\nInvalid operator selected!")


if result is not None:
 
    if result.is_integer():
        result = int(result)
        
    print(f"\nResult: {num1 if not isinstance(num1, float) or not num1.is_integer() else int(num1)} {op} {num2 if not isinstance(num2, float) or not num2.is_integer() else int(num2)} = {result}")
    print(f"Result type: {type(result)}")