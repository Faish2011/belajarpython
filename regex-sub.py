import re


text = "the quick brown fox"
text += "jumps over 12 lazy dogs!"

y = re.sub (r"\s", "_", text)

print (y)


x = re.sub (r"\s", "_", text, 2)

print (x)




































