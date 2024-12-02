print ("my calculator")
print ("-=-=-=-=-=-\n")

number1 = input ("number1: ")
number2 = input ("number2: ")

operator = input ('operator: ')

expression = f"{number1} {operator} {number2}"
result = eval (expression)

print (f'{number1} {operator} {number2} = {result}')










