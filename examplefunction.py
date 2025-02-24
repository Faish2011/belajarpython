def addition (num1, num2):
  result = num1 + num2  
  return f"{num1} + {num2} = {result}"  

number = int (input("enter a number to add: "))
loop = int (input("enter how many loops: "))

for i in range (1, loop + 1): 
  print (addition (number, i))  















































