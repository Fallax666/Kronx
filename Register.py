import random
from os.path import exists as file_exists
from Scripts import logo
from Scripts import colors
from Scripts import captcha

special_characters = "|}{:?><'[];/?.,+=_-)(*&^%$#@!~`"
number = "0123456789"
upper_character = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_character = "qwertyuiopasdfghjklzxcvbnm"


def register():
    captcha.begin()
    logo.kronx()
    while True:
        print(colors.OKGREEN + """         Insert username
               * Min 6 characters long
        """)
        user_name = input("››  ")
        if len(user_name) < 6:
            print("        Username lenghts is too short, please try again\n\n")
            continue
        else:
            while True:
                print("Username set : " + user_name + "\n")
                print("Insert password")
                print("""
                        * Atleast 8 characters long
                        * Should contain atleast 1 special character
                        * Minium 1 upper character
                        * Minium 1 lower character
                        * Has to contain atleast 1 digit""")
                password_contains_upper = False
                password_contains_special = False
                password_contains_lower = False
                password_contains_digit = False
                choice = input("››  ")
                if choice == user_name:
                    print("Password and username are similar, try again")
                    continue
                print("Confirm password\n")
                user_password = input("››  ")
                if user_password != choice:
                    print("Passwords don't match\n Try again\n")
                    continue
                else:
                    for x in special_characters:
                        for z in user_password:
                            if x == z:
                                password_contains_special = True
                    if password_contains_special is not True:
                        print("Password has no special characters\n Try again\n")
                        continue
                    if len(user_password) < 8:
                        print("Password is too short")
                        continue
                    for x in number:
                        for z in user_password:
                            if x == z:
                                password_contains_digit = True
                    for x in lower_character:
                        for z in user_password:
                            if x == z:
                                password_contains_lower = True
                    for x in upper_character:
                        for z in user_password:
                            if x == z:
                                password_contains_upper = True
                    if password_contains_digit is not True:
                        print("Password has no digits\n Try again\n")
                        continue
                    if password_contains_lower is not True:
                        print("Password has no lower\n Try again\n")
                        continue
                    if password_contains_upper is not True:
                        print("Password has no upper\n Try again\n")
                        continue
                    user_id = (str(user_password[0:1]) + str(random.randint(1000000001, 9999999999)))
                    if password_contains_special and password_contains_digit and password_contains_upper:
                        if password_contains_lower:
                            #
                            #     ---> TEMP DATABASE based on a text document
                            #
                            if file_exists("Data/Accounts"):
                                f = open("Data/Accounts", "w")
                                f.write(f">{user_name}>{user_id}>{user_password}>")
                                f.close()
                            else:
                                f = open("Data/Accounts", "x")
                                f.close()
                                f = open("Data/Accounts", "w")
                                f.write(f">{user_name}>{user_id}>{user_password}>")
                                f.close()
                                return
                                #
                                #     ________________________________________
                                #
                            break
                        else:   # If somehow the code has flaws
                            print("Password has no lower characters !")
                            register()
                            break
                    else:  # just in case
                        print("Something went wrong")
                        register()

            break
