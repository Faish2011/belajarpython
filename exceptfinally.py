student = {
  "name" : "Jaka",
  "address" : "Jakarta",
}

try:
  print (student)
except NameError:
  print ("student variable is not defined")
except:
  print ("An error occured!")
finally :
  print ("Script has run!")
  print ("The program stopped!")






























