#Level 2
#username = input("Please enter your username: ")
#if username == "Username":
    #print ("You are not allowed on this system.")

#Level 3
#username = input("Please enter your username: ")
#if username.isalpha():
    #clearance += 2
#else:
    #clearance += 1
#print ("You have level %i clearance" %(clearance))

#Level 4
#username = input("Please enter your username: ")
#username = username.upper()
#vowels = username.count("A") + username.count("E") + username.count("I") + username.count("O") + username.count("U")
#if username.isalpha():
    #clearance = 2
    #if vowels >= 3:
        #clearance += 1
        #if username[:1] == "A":
            #clearance += 1
#else:
    #clearance = 1
#print ("You have level %i clearance" %(clearance))

#Level 4+
username = input("Please enter your username: ")
username = username.upper()
vowels = username.count("A") + username.count("E") + username.count("I") + username.count("O") + username.count("U")
if username.isalpha():
    clearance = 2
    if vowels >= 3:
        clearance += 1
        if username[:1] == "A":
            clearance += 1
            if username[:len(username)//2] == username[len(username)//2:]:
                clearance += 1
else:
    clearance = 1
print ("You have level %i clearance." %(clearance))