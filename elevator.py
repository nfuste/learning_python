import time

items = [] 

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator")

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



def select_floor():
    floor_selection = valid_imput("Please enter the number for the floor you would like to visit:\n"
                                    "1. Lobby\n"
                                    "2. Human resources\n"
                                    "3. Engineering department\n",
                                    "1", "2", "3")
    if "1" in floor_selection:
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find yourself in the lobby")

        if "ID card" in items:
            print_pause("The clerk greets you, but she has already given you your"
                        "ID card, so there is nothing more to do here now.")
        else:
            items.append("ID card")
            print_pause("The clerk greets you and gives you your ID card.")

    elif "2" in floor_selection:
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself in the human resources department")
    elif "3" in floor_selection:
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself in the engineering department")

def loop_select_other_floor():
    while True:
        print_pause("Where would you like to go next?")
        select_floor()

intro()
select_floor()
loop_select_other_floor()
