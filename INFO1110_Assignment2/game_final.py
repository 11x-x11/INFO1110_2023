'''
Answer for Question 7 - PIAT: Improved Full Game.

Author: Ni Shaoqing
SID: 530532312
Unikey: shni6293
'''
import train
import mouse
import game
import sys
from datetime import datetime


# A function that check if all the files are the same as the file in master directory and fix it
def run_setup():
    from setup import installation, verification, current_date, logging
    master_path = "/home/game_master/"
    timestamp = current_date()
    now = datetime.strptime(timestamp, "%d %b %Y %H:%M:%S")
    date = now.strftime("%Y-%b-%d")
    time = now.strftime("%H_%M_%S")
    verify = verification(master_path, timestamp)
    logging(verify, date, time)
    if verify[-1] == "Abnormalities detected...":
        decision = input("Do you want to repair the game? ")
        if decision == "YES" or decision == "yes":
            install = installation(master_path, timestamp)
            logging(install, date, time)
            print('''Launching game...
.
.
.''')
            return False
        else:
            print('Game may malfunction and personalization will be locked.')
            warning = input('Are you sure you want to proceed? ')
            if warning == "YES" or warning == "yes":
                print('''You have been warned!!!
Launching game...
.
.
.''')
                return True
            else:
                sys.exit(1)
    else:
        print('''Launching game...
.
.
.''')
        return False


# An updated game_title
def game_title():
    logo = '''
       ____()()
      /      @@
`~~~~~\_;m__m._>o'''

    title = "Mousehunt"
    author = 'Shaoqing Ni'
    credits = '''
Inspired by Mousehunt© Hitgrab
Programmer - An INFO1110/COMP9001 Student
Mice art - Joan Stark and Hayley Jane Wakenshaw'''
    print(title)
    print(logo)
    print(credits)
    print()


# ask user to input name, if the name is invalid, name them to be Bob or generate a new name
def personalization():
    from name import is_valid_name, generate_name
    verif_of_game = run_setup()
    game_title()
    if verif_of_game is False:
        ask_for_name = input("What's ye name, Hunter? ").strip()
        if is_valid_name(ask_for_name.lower()) is False:
            print('''That's not nice!
I'll give ye 3 attempts to get it right or I'll name ye!
Let's try again...''')
            strike_idx = 1
            while strike_idx < 4:
                new_name = input("What's ye name, Hunter? ").strip()
                check_name = is_valid_name(new_name.lower())
                if check_name is True:
                    print(f'Welcome to the Kingdom, Hunter {new_name}!')
                    return new_name
                elif check_name is False:
                    print(f'Nice try. Strike {strike_idx}!')
                if strike_idx == 3:
                    print('I told ye to be nice!!!')
                    break
                strike_idx += 1
            player_name = generate_name(new_name.lower())
            print(f'Welcome to the Kingdom, Hunter {player_name}!')
        else:
            player_name = ask_for_name
            print(f'Welcome to the Kingdom, Hunter {player_name}!')
    elif verif_of_game is True:
        player_name = 'Bob'
        print(f'Welcome to the Kingdom, Hunter {player_name}!')
    return player_name


# ask the user if they wanna skip training or not
def ask_for_training():
    discussion = input('''Before we begin, let's train you up!
Press "Enter" to start training or "skip" to Start Game: ''')
    if discussion.strip().lower() != "skip":
        print()
        trap_name_and_e_flaog = train.main()
    else:
        trap_name_and_e_flaog = "Cardboard and Hook Trap", False
    return trap_name_and_e_flaog



# updated hunt with updated probability table and different enchant benfits
def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int, enchant: bool) -> tuple:
    hunts_without_catch = 0
    while True:
        print("Sound the horn to call for the mouse...")
        split_choice = input('Sound the horn by typing "yes": ').lower().strip().split()
        choice = " ".join(split_choice)
        cheese_idx = 0
        if trap_cheese is not None:
            arm_cheese = trap_cheese.lower().capitalize()
            while cheese_idx < len(cheese):
                if arm_cheese == cheese[cheese_idx][0]:
                    cheese_quantity = cheese[cheese_idx][1]
                    break
                cheese_idx += 1
        else:
            cheese_quantity = 0
        if choice == "yes" and cheese_quantity > 0:
            game.consume_cheese(trap_cheese, cheese)
            new_mouse = mouse.Mouse(trap_cheese, enchant)
            if new_mouse.get_name() is not None:
                print(f"Caught a {new_mouse.get_name()} mouse!")
                print(new_mouse.get_coat())
                if enchant is True and trap_cheese == "Cheddar" and new_mouse.get_name() == "Brown":
                    gold += new_mouse.get_gold()
                    points += (new_mouse.get_points() + 25)
                    enchant = False
                elif enchant is True and trap_cheese == "Marble" and new_mouse.get_name() == "Brown":
                    gold += (new_mouse.get_gold() + 25)
                    points += new_mouse.get_points()
                    enchant = False
                else:
                    gold += new_mouse.get_gold()
                    points += new_mouse.get_points()
                hunts_without_catch = 0
                print(f"My gold: {gold}, My points: {points}\n")
            else:
                print("Nothing happens.")
                hunts_without_catch += 1
                print(f"My gold: {gold}, My points: {points}\n")
        elif choice == "yes" and cheese_quantity <= 0:
            print("Nothing happens. You are out of cheese!")
            hunts_without_catch += 1
            print(f"My gold: {gold}, My points: {points}\n")
        elif choice == "stop hunt":
            return gold, points
        else:
            print("Do nothing.")
            print(f"My gold: {gold}, My points: {points}\n")
            hunts_without_catch += 1
        if hunts_without_catch >= 5:
            continue_choice = input("Do you want to continue to hunt? ")
            if continue_choice == "no":
                return gold, points
            else:
                hunts_without_catch = 0
                continue
        else:
            continue


# return relevant benefit according to the given cheese name
def get_benefit(cheese):
    if cheese == "Cheddar":
        return "+25 points drop by next Brown mouse"
    elif cheese == "Marble":
        return "+25 gold drop by next Brown mouse"
    elif cheese == "Swiss":
        return "+0.25 attraction to Tiny mouse"


def main():
    player_name = personalization()
    trap_name_and_e_flaog = ask_for_training()
    enchantment_status = trap_name_and_e_flaog[1]

    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    cheese_name = None
    points = 0
    count_hunt = 0

    while True:
        print(f'\nWhat do ye want to do now, Hunter {player_name}?')
        print(game.get_game_menu())
        while True:
            choice = input('Enter a number between 1 and 4: ')
            try:
                choice = int(choice)
            except ValueError:
                print('Invalid input.')
                continue
            if choice < 1 or choice > 4:
                print('Must be between 1 and 4.')
            else:
                break
        if choice == 1:
            break
        elif choice == 2:
            hunt_variable = hunt(gold, cheese, cheese_name, points, enchantment_status)
            enchantment_status = False
            gold = hunt_variable[0]
            points = hunt_variable[1]
        elif choice == 3:
            print()
            from shop import loop_welcome
            while True:
                if enchantment_status is False:
                    shop_variable = loop_welcome(gold, cheese, trap_name_and_e_flaog[0])
                    gold = shop_variable[0]
                    cheese = shop_variable[1]
                    break
                elif enchantment_status is True:
                    enchantment_trap = "One-time Enchanted" + " " + trap_name_and_e_flaog[0]
                    shop_variable = loop_welcome(
                        gold, cheese, enchantment_trap)
                    gold = shop_variable[0]
                    cheese = shop_variable[1]
                    break
        elif choice == 4:
            print()
            if count_hunt > 0:
                enchantment_status = False
            if enchantment_status is False:
                trap = shop_variable[2].lstrip("One-time Enchanted ")
                arm_trap_cheese_name = game.change_cheese(
                    name=player_name, trap=trap, cheese=cheese, e_flag=enchantment_status)
            else:
                arm_trap_cheese_name = game.change_cheese(
                    name=player_name, trap=shop_variable[2], cheese=cheese, e_flag=enchantment_status)
            if arm_trap_cheese_name is None:
                continue
            arm_trap = arm_trap_cheese_name[0]
            if arm_trap is None:
                trap_name_and_e_flaog[0] = "Cardboard and Hook Trap"
            cheese_name = arm_trap_cheese_name[1]


if __name__ == '__main__':
    main()
