# Author: SCT (ADMG) 10/27/21

food1 = input("What did he eat for lunch?\n")

food2 = input("What did she eat for lunch?\n")

if food1 == food2:
    print("You ate the same thing")
elif food1 < food2:
    print("She ate a better lunch")
elif food1 > food2:
    print("He ate a better lunch")
