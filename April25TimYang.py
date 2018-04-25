#Level 2
string = input("Please enter a sentece: ")
for i in range(0, len(string)):
    tempString = str(i)
    print (string[i] + "(" + tempString + ") ", end="")

#Level 3
string = input("Please enter a sentece: ")
print ("Spaces are at locations: ", end="")
for i in range(0, len(string)):
    tempString = str(i)
    if string[i] == " ":
        print (str(i) + " ", end="")

#Level 4
string = input("Please enter a sentece: ")
len(string)
count = 0
for i in range(0, len(string)):
    if string[i + count] == " ":
        string = string[:i + count] + "mouse" + string[i + 1 + count:]
        count += 4 
print (string)

#Level 4+
evenString = ""
oddString = ""
for x in range(0, len(string)):
    if x % 2 == 0:
        evenString += string[x]
    else:
        oddString += string[x]

print("Even string is: " + evenString)
print("Odd string is: " + oddString)