from Scripts import logo
from os.path import exists as file_exists
from Scripts import colors
import Register
user_name = []
var = False
count = 0
count2 = 3

random_string = "cuvantcheie"


def begin():
    logo.kronx()
    print("Insert username")
    choice = input(" ››  ")
    if not file_exists("Data/Accounts"):
        print(colors.WARNING + """
        Error
        Looks like database is corrupted

        You will have to create a new account !""")
        Register.register()
    else:
        count = 0
        count2 = 3
        f = open("test", "r")
        for x in f:
            count += 1
            user_name.append(x)
            print(user_name)




begin()