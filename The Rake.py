"""
The Rake: A Text Adventure
"""

__author__ = "Zac Buresh"

__date__ = "8/28/2018"

import sys

def KeyWord(key, inpt):
    """Takes an input and returns True if the key words are met"""
    inpt = inpt.lower()
    key = key.split(' ')
    ct = 0
    for item in key:
        if item in inpt:
            ct += 1
    if ct == len(key):
        return True
    else:
        return False
    
def Die():
    """Displays the death screen and stops the program"""
    print("YOU ARE DEAD")
    valid = False
    while valid == False:
        restart = input("Do you wish to restart? Yes/No: ")
        if restart == "Yes":
            Game()
            vaild = True
        elif restart == "No":
            sys.exit()
            vaild = True

def CheckInventory(item, Inventory):
    """Checks if an item is in the inventory"""
    for el in Inventory:
        if el == item:
            return True
    return False
    
def Game():
    """The entire game"""

    Inventory = []
    print()
    print("    The Rake: A Text Adventure")
    print("===================================")
    print("By Zac Buresh -- Created: 8/28/2017")
    print()
    print()
    print("You begin to gain conciousness. The only thing you can see is the orange glow from your digital clock.")
    print("It reads 3:35 AM. You just awoke from a nightmare which is why you lay in your bed paralyzed, scared to make a sound.")
    print("You wonder if you awoke because of the dream or because of something from the outside world. Eventually, you look")
    print("towards the foot of your bed and see a shadow very much like the one in the nightmare you had moments before. It must not")
    print("be real...but as soon as you look away, you hear foot steps rapidly scurring away out into the hall. The shadow is gone!")
    print("\nYou decide to go investigate! ")

    #LIGHTS
    action1 = input("\nType an action: ")
    action1 = action1.lower()
    while KeyWord("turn light", action1)== False and KeyWord("sleep", action1)== False:
        print("You shouldn't go after that thing while it is dark!")
        action1 = input("\nType an action: ")
        action1 = action1.lower()
    if KeyWord("turn light", action1)== True:
        print("You turn on the lamp next to you!")
        print("On your bedside table you see a family photo, your glasses, and a knife.")
    elif KeyWord("sleep", action1)== True:
        print("The creature lunges onto your back and claws your body, causing you to bleed out...")
        Die()

    #GLASSES
    requirement1 = 0
    while requirement1 == 0:
        action2 = input("\nType an action: ")
        action2 = action2.lower()
        while KeyWord("photo",action2)== False and KeyWord("glasses",action2)== False and KeyWord("knife",action2)== False:
            print("Despite the light being on, your eye sight is not the greatest.")
            action2 = input("\nType an action: ")
            action2 = action2.lower()
        if KeyWord("photo",action2)== True:
            print("You see your two daughters taking their first steps. You and your wife are standing across from them")
            print("with arms wide open to catch them! Speaking of your wife...where is she?")
        elif KeyWord("glasses",action2)== True:
            requirement1 += 1
            print("Ahhhhh that's much better. Now you can go check what that sound was!")
            print("Just as you put on your glasses you hear something crash out in the hallway.")
        elif KeyWord("knife",action2)== True:
            print("Feeling threatened and a little bit scared, you pick up the knife for self-defense.")
            Inventory.append("Knife")
            print("--Knife-- was added to your inventory!")

    #GET UP
    requirement2 = 0
    while requirement2 == 0:
        action3 = input("\nType an action: ")
        action3 = action3.lower()
        while KeyWord("photo", action3)== False and KeyWord("knife", action3)== False and KeyWord("up", action3)== False and KeyWord("bed", action3)== False:
            print("You can't go investigate without getting up. That would just be silly.")
            action3 = input("\nType an action: ")
            action3 = action3.lower()
        if KeyWord("photo", action3)== True:
            print("You see your two daughters taking their first steps. You and your wife are standing across from them")
            print("with arms wide open to catch them! Speaking of your wife...where is she?")
        elif KeyWord("knife", action3)== True:
            print("Feeling threatened and a little bit scared, you pick up the knife for self defense.")
            Inventory.append("Knife")
            print("--Knife-- was added to your inventory!")
        elif KeyWord("up", action3)== True:
            requirement2 += 1
            print("Your legs are wobbling but now you can go investigate that sound!")
            print("You slowly make your way to the hallway.")
        elif KeyWord("bed", action3)== True:
            requirement2 += 1
            print("Your legs are wobbling but now you can go investigate that sound!")
            print("You slowly make your way to the hallway.")

    #HALLWAY
    print("In the hallway, you see a shattered vase on the ground, tattered wallpaper,")
    print("and you notice that your two daughter's door is open.")
    requirement3 = 0
    while requirement3 == 0:
        action4 = input("\nType an action: ")
        action4 = action4.lower()
        while KeyWord("vase", action4)== False and KeyWord("wallpaper", action4)== False and KeyWord("door", action4)== False and KeyWord("room", action4)== False:
            print("You should probably check on your daughters.")
            action4 = input("\nType an action: ")
            action4 = action4.lower()
        if KeyWord("vase", action4)== True:
            print("This vase was pretty heavy. Something must've knocked it off.")
            print("You decide to pick up a shard of the vase for protection.")
            Inventory.append("Vase Shard")
            print("--Vase Shard-- was added to your inventory!")
        elif KeyWord("wallpaper", action4)== True:
            print("The wallpaper is torn in four long streaks. It looks like whatever that thing was, it has four claws.")
        elif KeyWord("door", action4)== True:
            requirement3 += 1
            print("You advance to your children's door. The room is lit up from the shining moon but a shadow is draped out across the floor.")
            print("On the window sill, your are terrified to see the silhouette of a hunched-over creature grasping one of your daughters in each of its hands!")
            if CheckInventory("Knife", Inventory)== True or CheckInventory("Vase Shard", Inventory)== True:
                print("The lanky and hairless creature stares at the weapon in your hand, turns around, and bounds out the window with your children.")
            else:
                print("The lanky and hariless creature sees that you are vulnerable and lunges at you and claws your heart out!")
                Die()
        elif KeyWord("room", action4)== True:
            requirement3 += 1
            print("You advance to your children's door. The room is lit up from the shining moon but a shadow is draped out across the floor.")
            print("On the window sill, you are terrified to see the silhouette of a hunched-over creature grasping one of your daughters in each of its hands!")
            if CheckInventory("Knife", Inventory)== True or CheckInventory("Vase Shard", Inventory)== True:
                print("The lanky and hairless creature stares at the weapon in your hand, turns around, and bounds out the window with your children.")
            else:
                print("The lanky and hariless creature sees that you are vulnerable and lunges at you and claws your heart out!")
                Die()
            
def main():

    Game()
        
if __name__ == "__main__":
    main()
