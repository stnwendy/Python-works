print("\t\t\tWelcome, user")
i=0
pword="password12345"

while i<5: 
    userPword=input("Type your password: ")
    if userPword!=pword:
        i=i+1
        print("Incorrect password. You have ", 5-i, " attempts left." )
        continue
    else:
        print("\nLogged in succesfully.")
        break
    
else:
    print("\nKicked out")
    

