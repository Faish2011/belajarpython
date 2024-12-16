print ("COMPARE PROJECT")
print ("==========\n")


num1 = input('Number 1 = ')
num2 = input('Number 2 = ')
operator = input('Operator (==, !=, <, >, <=, >=) = ')

expression = f"{num1} {operator} {num2}"

result = eval(expression)

print(f'{num1} {operator} {num2} = {result}')

















