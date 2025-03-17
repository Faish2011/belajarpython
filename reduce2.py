from functools import reduce

def addition (number1, number2):
    return number1 + number2

number_list = range (1,11)

x = reduce (addition, number_list)

print (x)





















































