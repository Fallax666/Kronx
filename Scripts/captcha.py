import random


def begin():
    print("""
     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP'
     """)
    tries = 3
    while True:
        if tries <= 0:
            print("You run out of tries")
            exit()
        print("\n")
        print("Input the following code")
        captcha = random.randint(100001, 999999)
        if len(str(captcha)) < 6:
            print("Internal error")
            exit()
        else:
            print(str(captcha))
            choice = input("    ›› ")
            if choice != str(captcha):
                tries -= 1
                print("You got it wrong, try again")
                print("Tries left " + str(tries))
            else:
                print("Succes")
                return True