'''
Answer for Question 5 - The Training Again from Assignment 1.

Author: Shaoqing Ni
SID: 530532312
unikey: shni6293
'''


def main():
    from q4 import intro_travel_to_camp, setup_trap, sound_horn, basic_hunt, complete_train, user_input
    e_flag = False
    travel_status = intro_travel_to_camp()
    if travel_status is False:
        return "Cardboard and Hook Trap", e_flag
    while True:
        cheddar = setup_trap()
        if cheddar is False:
            return "Cardboard and Hook Trap", e_flag
        else:
            horn_input = sound_horn()
            if horn_input is False:
                return cheddar[0], e_flag
        hunt_status = basic_hunt(cheddar[1], horn_input)
        complete_train(hunt_status)
        training = user_input(
            '\nPress Enter to continue training and "no" to stop training: ')
        if training == 'no' or (cheddar is not False and training is True):
            if cheddar[0] == 'Cardboard and Hook Trap':
                e_flag = False
                return cheddar[0], e_flag
            else:
                e_flag = True
                return cheddar[0], e_flag
        elif cheddar is False and training is True:
            return "Cardboard and Hook Trap", e_flag


if __name__ == '__main__':
    main()
