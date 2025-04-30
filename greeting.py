#import mymodule

#mymodule.greeting ("malik")

#msg = "a module author is "+mymodule.author
#print (msg)

#import mymodule as mm

#mm.greeting ("malik")

#msg = "a module author is "+mm.author
#print (msg)

from mymodule import greeting, author

greeting ("malik")

msg = "a module author is"+author
print (msg)






















