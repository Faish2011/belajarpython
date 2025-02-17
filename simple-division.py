print ("project error handling")
print ("-=-=-=-=-=-=-=-=-=-=-=-")

try:
    first_num = int (input("input number one: "))
    sec_num = int (input("input number two: "))

    if first_num == 0 or sec_num == 0:
        raise ZeroDivisionError ("numbers cannot be zero")

    number = {
        "first": first_num,
        "sec": sec_num,
    }
    print (number)

except ZeroDivisionError:
    print ("cant be 0")

except ValueError:
    print ("error: please input as numbers")
















































