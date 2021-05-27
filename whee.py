#this is basically me being bizarre so be warned haha
running = True

while running:
    name = input("Hello!, please tell me who you are: ")
    
    if name == "Blimpulus Blimpotomus Smith":
        print("ALARM! ALARM! SOMEONE WENT IN!")
        break
    
    if name == "Lucy":
        print("Hello Woat Two!")
        print("heh")
    elif name == "Nobody":
        print("Nobody is incorrect.")
        print("Try again, please!")
        print(" ")
        print("P.S.")
        print("There are five other special names.")
        import random
        easter_eggs = ["Blimpulus Blimpotomus Smith", "Lucy", "the magus", "Doctor Strange", "Karenna"]
        print("Hint: try '" + (random.choice(easter_eggs)) + "'")
        continue
    elif name == ("the magus"):
        print("COME ON")
        print("I thought this would work")
        print("..or do you not have a real name?")
        print("I doubt that...")
        print("So, so, so.")
        print("You're just Not Telling. What a shame.")   
    else: print("Hey " + name + "!")
    
    if name == "Doctor Strange":
        print("Weclome to my loop ;)")
        continue
    elif name == "Karenna":
        print("Welcome back! You're our favorite! ;)")
    elif name == "Lucy":
        next
    elif name == "the magus":
        next
        #There's probably some way to combine "Lucy" and "the magus" here but idk what it is
    else: print("You're not our favorite :(")

    if name == "Lucy":
        print("Tootles!")
    else: print("Goodbye!")
    
    
    running = False

 
