import re

text = "the quick brown fox"
text += "jumps over 12 lazy dogs!"

x = re.findall (r"\d", text)


print (x)

y = re.findall (r"cats", text)

print (y)

z = re.search (r"\d", text)

print (z)

print (z.span ())

print (z.group ())

















