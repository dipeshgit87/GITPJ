print("WELCOME TO THE MAGIC FOREST!!!!!!!!!!!\n")

direction = input("Go north or south: ").strip().lower()
if direction == 'south':
    print("GAME OVER!!!!!")
else:
    print("You're into the next round")
    uin = input("Cross the river or Follow the path:").strip().lower()
    if uin == 'Cross the river':
        print("GAME OVER!!!!!")
    else:
        print("You're into the next round")
        choose = input("Choose fairy, orge or elf:").strip().lower()
        if choose == 'fairy' or choose == 'ogre':
            print("GAME OVER!!!!!")
        else:
            print("Congratulations you have won the game🎉🎉🎈")