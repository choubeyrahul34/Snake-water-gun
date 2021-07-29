import random

print("!!!!!!!!!!!!!!Rules of the Game!!!!!!!!!!!!!!!!")
print("You have to type 's' for snake 'w' for water and 'g' for gun")
print("and computer chooses automatically and what computer choses, it display on screen after result.")

print("                                                                                                                                          ")
print("***************************************************************************************************")
print("                                                                                                                                          ")

print("If you computer choose 'Snake' and you chose 'Water' then you will be lose beacuse the Snake will drink all the Water")
print("If you computer choose 'Snake' and you chose 'Gun' then you will be win beacuse Gun will kill the Snake ")
print("And so on")
print("                                                                                                                                          ")

#***************************************************************************************************************************


def gamewin(comp, you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
 
    elif comp=="w":
        if you=="s":
            return True
        elif you=="g":
            return False

    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True


print("Computer's Turn...  To choose from Snake(s) Water(w) Gun(g)")
print("Computer's chose..  Now Your's turn ")
randNum = random.randint(1,3)
if randNum==1:
    comp = 's'
elif randNum==2:
    comp = 'w'
elif randNum==3:
    comp = 'g'

you = input("Enter what's in your mind from Snake, Water, Gun ||Type 's' for snake 'w' for water 'g' for gun||   :   ")
you = you.lower()
a = gamewin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a==None:
    print("This game is tie!!")

elif a:
    print("You win!!")

else:
    print("You lose!!")