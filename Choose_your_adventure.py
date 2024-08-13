print ("Hello human person! I welcome you on your journey!")
human = input("What is your name? ")
print (human + " sounds weird, but okay, lol.")

# Code for making the text red.
death = "\033[0;31mYou died.\033[0m"

print ("You should probably know, this journey won´t be easy and you might not survive it. Do you want to continue? write yes or no.")

choice = input().lower() 
if choice == "yes":
    print ("Good choice! Our first stop is visiting a haunted house where many people died.")
    print ("A ghost of a beautiful woman without a head appears to you and asks you if you'll help her find her missing body part. Will you help her, " + human + "?" )
    choice1 = input().lower()
    if choice1 == "yes":
        print("You have found her head in a suspicious-looking chest. Under it lies a treasure. Will you take the treasure too?")
        choice2 = input().lower() 
        if choice2 == "yes":
            print("The treasure is cursed and you brought a plague upon mankind.")
            print(death)
        elif choice2 == "no":
            print("You safely returned the head to the ghost lady and she finally found peace.")
            print("Your next stop is a dark forest where it is said that the trees whisper secrets. As you walk deeper, you hear the whispers growing louder.")
            print("One tree in particular seems to call out your name. Do you approach it? Yes or no?")
            choice3 = input().lower()
            if choice3 == "yes":
                print("The tree reveals a hidden pathway leading to an ancient temple. Inside, you find a powerful artifact. However, it is guarded by a fierce dragon.")
                print("Do you attempt to take the artifact or leave it and exit the temple? Type 'take' or 'leave'.")
                choice4 = input().lower()
                if choice4 == "take":
                    print("The dragon awakens and breathes fire, but you manage to grab the artifact. You now possess unimaginable power and you used mind control to calm down the dragon. You managed to escape and after your near death experiences decided you´re never leaving the house again. You´ve lived hapilly ever after.")
                elif choice4 == "leave":
                    print("You choose to leave the artifact untouched, but the dragon awakens because he can smell your scent. He thinks you smell quite tasty so he eats you.")
                    print(death)
            elif choice3 == "no":
                print("You ignore the tree’s call and continue walking. However, the whispers drive you mad, and you lose your way in the forest.")
                print(death)
    elif choice1 == "no":
        print("The woman took your head instead and now she´s not that beautiful anymore.")
        print(death)
elif choice == "no":
    print ("Someone left a banana peal on the ground and you slipped on it while you were trying to leave.")
    print(death)