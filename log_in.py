print("TEST")
special_characters = "|}{:?><'[];/?.,+=_-)(*&^%$#@!~`"
number = "0123456789"
upper_character = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_character = "qwertyuiopasdfghjklzxcvbnm"
password = "H@CKER666"
counter_0 = 0
counter_1 = 1


for x in upper_character:
    for z in password:
        counter_0 += 1
        counter_1 += 1
        if x == z:
            print("Match")
            print(z)