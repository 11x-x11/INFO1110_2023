'''
Answer for Question 5 - The Training Again

Name: Shaoqing Ni
SID: 530532312
unikey: shni6293

'''

# import functions from q4 except for the intro part
def q4_main():
    from q4 import setup_trap, sound_horn, basic_hunt, complete_train
    cheddar = setup_trap()
    horn_input = sound_horn()
    hunt_status = basic_hunt(cheddar[1], horn_input)
    complete_train(hunt_status)
    return cheddar[0]


def main():
    # from q4 import the intro functions
    from q4 import intro_travel_to_camp
    intro_travel_to_camp()
    Status = False
    # loop until the Status = True
    while not Status:
        Trap = q4_main()
        # Ask the user to decide whether continue training or not
        training = input(
'\nPress Enter to continue training and "no" to stop training: ')
        # if the user input "no", end the loop by setting Status be True
        if training == 'no':
            Status = True
    return Trap


if __name__ == '__main__':
    main()
