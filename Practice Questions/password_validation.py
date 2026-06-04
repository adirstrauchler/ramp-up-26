import re
def validate_pasword():
    while True:
        password = input("Create a pasword with \n a) 8 characters \n b) a number \n c) an upercase letter \n d) a lowercase letter \n e) a special character \n")
        if len(password) < 8:
            print("your password is too short")
        elif not re.search("[a-z]+", password):
            print("your password does not contain a lowercase letter")
        elif not re.search("[A-Z]+", password):
            print("your password does not contain an upercase letter")
        elif not re.search("\d+", password):
            print("your password does not contain a number")
        elif not re.search("\W+", password):
            print("your password does not contain a special character")
        else:
            print("password set")
            return
if __name__ == "__main__":
    validate_pasword()