'''
Write your answer for the full OO version of the game here.

Author: Ni shaoqing
SID: 530532312
Unikey: shni6293
'''


from hunter import Hunter
from name import generate_name
from interface import Interface
import train
import game_final


# ask user to input name, if the name is invalid, name them to be Bob or generate a new name
def ask_for_name(success_setup):
    status = False
    hunt = Hunter()
    if success_setup is False:
        ask_for_name = input("What's ye name, Hunter? ").strip()
        hunt.set_name(ask_for_name)
        if hunt.name != ask_for_name.strip():
            print('''That's not nice!
    I'll give ye 3 attempts to get it right or I'll name ye!
    Let's try again...''')
            strike_idx = 1
            while strike_idx < 4:
                new_name = input("What's ye name, Hunter? ").strip()
                hunt.set_name(new_name.strip())
                if hunt.name != new_name.strip():
                    print(f'Nice try. Strike {strike_idx}')
                elif hunt.name == new_name.strip():
                    status = True
                    break
                if strike_idx == 3:
                    print('I told ye to be nice!!!')
                    break
                strike_idx += 1
            if status is False:
                player_name = generate_name(new_name.lower().strip())
                hunt.set_name(player_name.strip())
        print(f'Welcome to the Kingdom, Hunter {hunt.name}!')
    elif success_setup is True:
        hunt.set_name('Bob')
        print(f'Welcome to the Kingdom, Hunter {hunt.name}!')
    return hunt


# ask the user if they wanna skip training or not
def ask_for_training(hunt_class):
    discussion = input('''Before we begin, let's train you up!
Press "Enter" to start training or "skip" to Start Game: ''')
    if discussion.strip().lower() != "skip":
        print()
        trap_name_and_e_flaog = train.main()
        hunt_class.trap.set_trap_name(trap_name_and_e_flaog[0])
        hunt_class.trap.set_one_time_enchantment(trap_name_and_e_flaog[1])
    else:
        hunt_class.trap.set_trap_name("Cardboard and Hook Trap")
        hunt_class.trap.set_one_time_enchantment(False)
    return hunt_class


def main():
    setup_status = game_final.run_setup()
    game_final.game_title()
    hunt = ask_for_name(setup_status)
    hunt_class = ask_for_training(hunt)

    game_interface = Interface(player=hunt_class)
    game_interface.set_player(hunt_class)

    while True:
        print(f'\nWhat do ye want to do now, Hunter {game_interface.player.name}?')
        print(game_interface.get_menu())
        choice = input('Enter a number between 1 and 4: ')
        try:
            choice = int(choice)
        except ValueError:
            choice = choice
        if choice == 3 or choice == 4:
            print()
        game_interface.move_to(choice)


if __name__ == '__main__':
    main()

