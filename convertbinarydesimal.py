print ("CONVERT APP FROM BINARY TO DESIMAL OR DESIMAL TO BINARY")

user_input = input ("enter a binary number like 1010 or desimal number like 10:")

if user_input.isdigit() and '2' not in user_input and '3' not in user_input and '4' not in user_input and '5' not in user_input and '6' not in user_input and '7' not in user_input and '8' not in user_input and '9' not in user_input:

    decimal_value = int (user_input, 2)

    print (f"binary: {user_input} -> decimal: {decimal_value}")

else: 

    binary_value = bin (int(user_input))[2:]


    print (f"decimal: {user_input} -> binary: {binary_value}")
















