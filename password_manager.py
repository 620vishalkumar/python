# from cryptography.fernet import Fernet


# def view(f,encrypted_message):
#     print((f.decrypt(encrypted_message)).decode())


# key=Fernet.generate_key()
# f=Fernet(key)
# message=input("enter your message: ")
# message=message.encode()   #encode helps us to encode our message in byte string

# encrypted_message=f.encrypt(message) #encrypting the data with the help of key

# view(f,encrypted_message)

#*********************** let's make a password manager *************************

# from cryptography.fernet import Fernet
# while True:
#     choice=input("enter add/change/view/quit : ")
#     if choice.strip().lower()=="add":
#         username=input("enter your username : ")
#         password=input("enter your password : ")
#         with open("pass.txt","a") as file:
#             file.write(f"{username}     |    {password}\n")
#     elif(choice.strip().lower()=="quit"):
#         quit()
#     elif(choice.strip().lower()=="change"):
#         with open("pass.txt","a+") as file:
#             cng=file.read()
#             old=input('enter your username or password to change : ')
#             new=input("enter your new password or username : ")
#             cng.replace(old,new)


    
from cryptography.fernet import Fernet

#key=Fernet.generate_key()

key=b'2Z79iZBnwFHH5dCRCs_VHV3eXpZLS64OiG03fsI42I4='

f=Fernet(key)
mp=input("enter your master password to access : ")
mp=f.encrypt(mp.encode())

def add(f):
    username=input("enter your username : ")
    password =input("enter your password : ")
    password=f.encrypt(password.encode())
    with open("key.key","a") as file:
        file.write(f"{username}|{password.decode()}\n")

    

def view(f):
    with open("key.key","r")as file:
        li=file.readlines()
        for i in li:
            i=i.rstrip()
            username,password = i.split('|')
            print(f"username : {username} | password : {f.decrypt(password.encode()).decode()}")

if f.decrypt(mp) == b'vishal':
    while True:
        choice=input("choose an option add or view or quit : ")
        choice=choice.strip().lower()

        if(choice=="add"):
            add(f)
        elif choice=="view":
            view(f)
        elif choice=="quit":
            break




    

