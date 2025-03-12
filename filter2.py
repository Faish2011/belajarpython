numbers = range (1,101)


def is_even (n):
  return n % 2 == 0  


even_numbers = filter (is_even, numbers)

print (even_numbers)
print (list (even_numbers))

odd_numbers = filter (lambda n : n % 2 == 1, numbers)
print (odd_numbers)
print (list (odd_numbers))











































