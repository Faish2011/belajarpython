def factorial (number):
    if number <= 1:
        return 1
    else:
        result = number * factorial (number - 1)
        return result 
print (factorial (3))








































