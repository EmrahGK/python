import json

class User():
    __init__(self, data):
        self.username = username

global currentUser

def register():
    username = input("Username:")
    passwd = input("Password:")
    passwdtry = input("Retry Password:")
    mail = input("Mail:")
    phone = input("Phone Number:")
    if(passwd != passwdtry):
        print("Passwords are incorrect.Try again")

    user = User({
        "username":username
        "password":passwd
    })

    return 0
try:
    register()

except:
    pass
