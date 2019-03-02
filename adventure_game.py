import time
import random


# Sets a pause between the messages to print
def print_pause(text):
    print(text)
    time.sleep(2)


# Checks for a valid imput. Keeps repeating until it gets one
def valid_imput(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand")
    return response


# Play the game!
def play_game():
    items = []
    enemy = random.choice(["pirate", "dragon", "zombie", "vampire"])
    weapon = random.choice(["gun", "dagger", "katana", "bow"])
    intro(enemy, weapon)
    where_to_go(items, enemy, weapon)


# Welcomes you to the game
def intro(enemy, weapon):
    print_pause("You find yourself standing in an open field, filled with"
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                + weapon + ".")
    print_pause("\n")


# Player must choose between the house and the cave
def where_to_go(items, enemy, weapon):
    choice = valid_imput("Enter 1 to knock on the door of the house.\n"
                         "Enter 2 to peer into the cave.\n"
                         "What would you like to do?\n"
                         "(Please enter 1 or 2.)\n", "1", "2")

    if "1" in choice:
        house(items, enemy, weapon)

    if "2" in choice:
        cave(items, enemy, weapon)


# Things that happen to the player in the house
def house(items, enemy, weapon):

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out"
                "steps a " + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")

    if "cool_weapon" not in items:
        print_pause("You feel a bit under-prepared for this, whith only "
                    "having a tiny " + weapon)

    choice2 = valid_imput("Would you like to (1) fight or (2) run away?\n",
                          "1", "2")

    if "1" in choice2:
        if "cool_weapon" in items:
            win(enemy)
        else:
            loose(enemy, weapon)

    if "2" in choice2:
        print_pause("You run back into the field. Luckily, you don't seem to "
                    "have been followed")

        field(items, enemy, weapon)


# Things that happen to the player in the cave
def cave(items, enemy, weapon):
    if "cool_weapon" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        print_pause("\n")

        field(items, enemy, weapon)

    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of methal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly " + weapon + " and take the sword "
                    "with you.")
        print_pause("You walk back out to the field.")
        print_pause("\n")

        items.append("cool_weapon")
        field(items, enemy, weapon)


# Things that happen to the player in the field
def field(items, enemy, weapon):
    where_to_go(items, enemy, weapon)


# This happens if the user wins
def win(enemy):
    print_pause("As the " + enemy + " moves to atack, you unsheath your "
                "new sword")
    print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                "brace "
                "yourself for the attack")
    print_pause("But the " + enemy + " takes one look at your shiny new toy "
                "and runs away!")
    print_pause("You have rid the town of the " + enemy + ". You are "
                "victorious!")

    play_again()


# This happens if the user looses
def loose(enemy, weapon):
    print_pause("You do your best...")
    print_pause("but your " + weapon + " is no match for the " + enemy)
    print_pause("You have been defeated!")

    play_again()


# This asks the user if he/she wants to play again
def play_again():
    repeat = valid_imput("Would you like to play again? (y/n)\n", "y", "n")

    if "y" in repeat:
        print_pause("Excellent! Restarting the game...")
        play_game()

    if "n" in repeat:
        print_pause("Thanks fot playing! See you next time.")

    # THE END


play_game()
