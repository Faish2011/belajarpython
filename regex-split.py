import re


text = "the quick brown fox"
text += "jumps over 12 lazy dogs!"

y = re.split (r"\s", text)

print (y)

x = re.split (r"\s", text, 2)
print (x)

































