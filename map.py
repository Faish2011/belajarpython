def cap_name (name):
    return name.capitalize ()

names = ['andi', 'benny', 'chika', 'dodi']
proper_names = []

for name in names: 
    proper_names.append (cap_name(name))

print (proper_names)

proper_names = map (cap_name, names)
print (proper_names)
print (list (proper_names))






























































