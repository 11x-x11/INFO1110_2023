'''
Answer for Question 4 - The Training

Name: Shaoqing Ni
SID: 530532312
unikey: shni6293

'''


# check if user enters ESC + Enter
def user_input(prompt):
    user_input = input(prompt)
    if user_input == chr(27):
        return True
    return user_input.strip().lower()


# Function to introduce the camp and travel to the Meadow
def intro_travel_to_camp():
    print('''Larry: I'm Larry. I'll be your hunting instructor.
Larry: Let\'s go to the Meadow to begin your training!''')
    travel_status = user_input("Press Enter to travel to the Meadow...")
    if travel_status == True:
        return False
    print('''Travelling to the Meadow...
Larry: This is your camp. Here you'll set up your mouse trap.''')
    return True



# Function to set up the trap and get the user's choice
def setup_trap():
    Traps = ("High Strain Steel Trap", "Hot Tub Trap",
             "Cardboard and Hook Trap")
    print("Larry: Let's get your first trap...")
    view_traps = user_input("Press Enter to view traps that Larry is holding...")
    if view_traps == True:
        return False
    print(f'''Larry is holding...
Left: {Traps[0]}
Right: {Traps[1]}''')
    choice = user_input('Select a trap by typing "left" or "right": ')
    if choice == "left" or choice == "right":
        if choice == "left":
            choice_of_trap = Traps[0]
        else:
            choice_of_trap = Traps[1]
        print(f'''Larry: Excellent choice.
Your "{choice_of_trap}" is now set!
Larry: You need cheese to attract a mouse.
Larry places one cheddar on the trap!''')
        cheddar = 1
    elif choice is True:
        choice_of_trap = Traps[2]
        cheddar = 0
        return False
    else:
        print('''Invalid command! No trap selected.
Larry: Odds are slim with no trap!''')
        cheddar = 0
        choice_of_trap = Traps[2]
    return choice_of_trap, cheddar


# Function to sound the horn
def sound_horn():
    print("Sound the horn to call for the mouse...")
    horn_input = user_input("Sound the horn by typing \"yes\": ")
    if horn_input is True:
        return False
    return horn_input


# Function to perform the basic hunt and check if successful
def basic_hunt(cheddar=None, horn_input=None):
    if cheddar == 1 and horn_input == "yes":
        print("Caught a Brown mouse!")
        hunt_status = True
    else:
        if (cheddar == 1 and horn_input != "yes") or (cheddar == 0 and horn_input == "yes"):
            print("Nothing happens.")
            print("To catch a mouse, you need both trap and cheese!")
        elif cheddar == 0 and horn_input != "yes":
            print("Nothing happens.")
        else:
            return
        hunt_status = False
    return hunt_status


# Function to check if hunt status and display a success message
def complete_train(hunt_status):
    if hunt_status is True:
        print('''Congratulations. Ye have completed the training.
Good luck~''')


# Main function to run the program
def main():
    travel_status = intro_travel_to_camp()
    if travel_status == False:
        return "Cardboard and Hook Trap"
    cheddar = setup_trap()
    if cheddar == False:
        return False
    else:
        horn_input = sound_horn()
        if horn_input is False:
            return cheddar[0]
    hunt_status = basic_hunt(cheddar[1], horn_input)
    complete_train(hunt_status)


if __name__ == '__main__':
    main()

