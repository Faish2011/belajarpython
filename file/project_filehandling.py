with open ("myBio.txt", "w") as file:
    file.write ("hello, my name is Faishal.\n")
    file.write ("i am a python developer who enjoys learning new things.\n")

with open ("myBio.txt", "a") as file:
    file.write ("in my free time, i like to read tech blogs and play chess")

with open ("myBio.txt", "r") as file:
    content = file.read ()
    print ("contents of myBio.txt: \n")
    print (content)















































