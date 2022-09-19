from Scripts import colors
while True:
    print(colors.WARNING + '''
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░██╗░░██╗██████╗░░█████╗░███╗░░██╗██╗░░██╗░░░░░░░░
        ░░░░░░░░██║░██╔╝██╔══██╗██╔══██╗████╗░██║╚██╗██╔╝░░░░░░░░
        ░░░░░░░░█████═╝░██████╔╝██║░░██║██╔██╗██║░╚███╔╝░░░░░░░░░
        ░░░░░░░░██╔═██╗░██╔══██╗██║░░██║██║╚████║░██╔██╗░░░░░░░░░
        ░░░░░░░░██║░╚██╗██║░░██║╚█████╔╝██║░╚███║██╔╝╚██╗░░░░░░░░
        ░░░░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ''')
    print(colors.CRED + "                   1.) ————► Register")
    print(colors.WARNING + "                   2.) ————► Log in")
    print(colors.CRED + "                   3.) ————► Reset password")
    print("")
    print(colors.CRED + "                   0.) ————► Exit")
    print("")
    choice = input(" ››  ")
    if choice != "1" and choice != "2" and choice != "3" and choice != "0":
        print(str(choice) + "is not a valid option\n Please try again !")
        continue
    if choice == "1":
        print("")
    if choice == "2":
        print("")
    if choice == "3":
        print("")
    if choice == "0":
        exit()





