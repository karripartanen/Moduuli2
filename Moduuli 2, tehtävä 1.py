UserName = input("Hi there, what is your name?") #declares variable as the asked username
while UserName == "": #declares that while username is empty, the system will ask again
    UserName = input("You must have a name of some kind, please try again!")
print("Hi "+UserName+", nice to meet you!")
