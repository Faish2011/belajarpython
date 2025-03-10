print ("ARGS AVERAGE")
print (f'{20 * '='}')

def rata (*angka):
    result = 0
    for ang in angka:
        result += ang

    average = result / len (angka)
    print (result)
    print (average)

rata (1,2,3,4)



































