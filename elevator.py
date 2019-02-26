import time

items = [] 

# Sets a pause between the messages to print
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

# Welcomes you to the game
def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator")

# Checks for a valid imput. Keeps repeating until it gets one
def valid_imput(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_pause("Sorry, I don't understand")
    return response

# User chooses which floor to go
def select_floor():
    floor_selection = valid_imput("Please enter the number for the floor you would like to visit:\n"
                                    "1. Lobby\n"
                                    "2. Human resources\n"
                                    "3. Engineering department\n",
                                    "1", "2", "3")

    # This happens if the user selects the first floor (Lobby)
    if "1" in floor_selection:
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find yourself in the lobby")

        # Check wether user has ID card or not. If they already have the ID card, print
        # a message saying that there's nothing more to do here. If not, it adds it to the
        # items list
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already given you your"
                        "ID card, so there is nothing more to do here now.")
        else:
            print_pause("The clerk greets you and gives you your ID card.")
            items.append("ID card")

    # This happens if the user selects the second floor (Human Resources)
    elif "2" in floor_selection:
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself in the human resources department")

        # Checks if the player already has the handbook, they should get a message saying there's nothing
        # more to do here.
        if "Handbook" in items:
            print_pause("The HR folks are busy at their desks")
            print_pause("There doesn't seem to be much to do here")

        # Otherwise (they don't yet have the handbook), the HR manager should approach them
        else:
            print_pause("The head of HR greets you")

            # And if they have their ID card, the HR manager should give them the handbook
            if "ID card" in items:
                print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
                items.append("Handbook")
            
            # Otherwise, they should be told they first need the ID card
            else:
                print_pause("He has something for you, but says he can't  give it to you until you go get your ID card.")

    
    # This happens if the user selects the third floor
    elif "3" in floor_selection:
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself in the engineering department")

# This makes the user select another floor
def loop_select_other_floor():
    while True:
        print_pause("Where would you like to go next?")
        select_floor()

intro()
select_floor()
loop_select_other_floor()
