print ("FACTORIAL CALCULATOR")
print (f"{10 * '='}")
def factorial (number):
    if number <= 1:
        return 1
    else:
        result = number * factorial (number - 1)
        return result

number = int (input())
print (factorial (number))




















































