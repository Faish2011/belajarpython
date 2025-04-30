import hashlib 

mypassword = "password54321"
encodedPassword = mypassword.encode ('utf-8')

hashedPassword = hashlib.md5 (encodedPassword).hexdigest ()

print (hashedPassword)










































