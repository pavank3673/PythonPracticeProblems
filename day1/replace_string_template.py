str = "Hello <<UserName>>, How are you?"
user_name = input("Enter username : ")
if len(user_name) < 3:
    print("Ensure user name has min 3 char")
else:
    str = str.replace("<<UserName>>",user_name)
    print(str)

