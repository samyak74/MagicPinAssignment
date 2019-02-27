# MagicPin assignment application development
# Name: Samyak Jain, Roll no: 15103154
import re
def convert(string): 
    li = list(string.split(",")) 
    return li 
    
user_input = input("Enter the password in comma seperated values: ")

passwords = convert(user_input)
#print(passwords)
flag = 0
for password in passwords:
	while True:
            #print(password)
	    if (len(password)<6):
	        flag = -1
	        print(password)
	        print("Failure",end= " ")
	        print("Password must be at least 6 characters long.")
	        break
	    if (len(password)>12):
	    	flag = -1
	    	print(password)
	    	print("Failure",end= " ")
	    	print("Password must be at max 12 characters long.")
	    elif not re.search("[a-z]", password): 
	        flag = -1
	        print(password)
	        print("Failure",end= " ")
	        print("Password must contain at least one letter from [a-z].")
	        break
	    elif not re.search("[A-Z]", password): 
	        flag = -1
	        print(password)
	        print("Failure",end= " ")
	        print("Password must contain at least one letter from [A-Z].")
	        break
	    elif not re.search("[0-9]", password): 
	        flag = -1
	        print(password)
	        print("Failure",end= " ")
	        print("Password must contain at least one letter from [0-9].")
	        break
	    elif not re.search("[*$#=@]", password): 
	        flag = -1
	        print(password)
	        print("Failure",end= " ")
	        print("Password must contain at least one letter from [*$#=@].")
	        break
	    elif re.search("[%!)(]",password):
	    	flag= -1
	    	print(password)
	    	print("Failure",end= " ")
	    	print("Password cannot contain %!(")
	    	break
	    elif re.search("\s", password): 
	        flag = -1
	        break
	    else: 
	        flag = 0
	        print(password)
	        print("Success") 
	        break
