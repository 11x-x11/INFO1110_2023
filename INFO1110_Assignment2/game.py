'''
This file should borrow code from your Assignment 1.
However, it will require some modifications for this assignment.

Author: Ni Shaoqing
SID: 530532312
Unikey: shni6293
'''


import random
import q1


# returns a game menu string.
def get_game_menu():
    return ('''1. Exit game
2. Join the Hunt
3. The Cheese Shop
4. Change Cheese''')


# Use function from name.py to test if name is valid and display welcome message
def ye_name():
    from name import is_valid_name_old
    user_name = input("\nWhat's ye name, Hunter?\n")
    state = is_valid_name_old(user_name)
    if state is True:
        print(f'Welcome to the Kingdom, Hunter {user_name}!')
        return user_name
    else:
        print('Welcome to the Kingdom, Hunter Bob!')
        return "Bob"


# using functions from train.py and add new features "ESC" to skip during training
def train_or_not(player_name):
    from train import main
    discussion = input('''Before we begin, let's train you up!
Press "Enter" to start training or "skip" to Start Game: ''').strip().lower()
    if discussion == "skip":
        trap = "Cardboard and Hook Trap"
        menu(player_name, trap)
    else:
        print()
        trap = main()
        menu(player_name, trap[0])


def get_benefit(cheese):
    if cheese == "Cheddar":
        return "+25 points drop by next Brown mouse"
    elif cheese == "Marble":
        return "+25 gold drop by next Brown mouse"
    elif cheese == "Swiss":
        return "+0.25 attraction to Tiny mouse"


def change_cheese(name: str, trap: str, cheese: list, e_flag=False) -> tuple:
    while True:
        print(f'Hunter {name}, you currently have:')
        i = 0
        while i < len(cheese):
            print(f'{cheese[i][0]} - {cheese[i][1]}')
            i += 1
        print()
        select_cheese_name = input("Type cheese name to arm trap: ")
        if select_cheese_name.lower().strip() == "back":
            return False, None
        j = 0
        found_cheese = False
        while j < len(cheese):
            chosen_cheese_name = select_cheese_name.lower().strip()
            if chosen_cheese_name.lower().strip() == str(cheese[j][0]).lower():
                enchantament = get_benefit(chosen_cheese_name.capitalize())
                found_cheese = True
                break
            j += 1
        if found_cheese is True:
            if e_flag is True:
                print(f'Your {trap} has a one-time enchantment granting {enchantament}.')
            if cheese[j][1] > 0:
                arm_trap_or_not = input(f"Do you want to arm your trap with {cheese[j][0]}? ")
                if arm_trap_or_not.lower().strip() == "yes":
                    print(f'{trap} is now armed with {cheese[j][0]}!')
                    return True, cheese[j][0]
                elif arm_trap_or_not.lower().strip() == "no":
                    print()
                    continue
            else:
                print('Out of cheese!\n')
                continue
        elif found_cheese is False:
            print("No such cheese!\n")
            continue
        return False, None


def consume_cheese(to_eat: str, cheese: list) -> tuple:
    i = 0
    while i < len(cheese):
        if to_eat == str(cheese[i][0]):
            if cheese[i][1] > 0:
                cheese[i][1] = cheese[i][1] - 1
                break
        i += 1


def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int) -> tuple:
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
            consume_cheese(trap_cheese, cheese)
            Random = random.random()
            if Random <= 0.5:
                print("Caught a Brown mouse!")
                gold += 125
                points += 115
                hunts_without_catch = 0
                print(f"My gold: {gold}, My points: {points}\n")
            elif Random > 0.5:
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
            continue_choice = input("Do you want to continue to hunt? ").lower().strip()
            if continue_choice == "no":
                return gold, points
            else:
                hunts_without_catch = 0
                continue
        else:
            continue


def menu(player_name, trap):
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    cheese_name = None
    points = 0
    while True:
        print(f'\nWhat do ye want to do now, Hunter {player_name}?')
        print(get_game_menu())
        choice = input()
        if choice == "1":
            break
        elif choice == "2":
            hunt_variable = hunt(gold, cheese, cheese_name, points)
            gold = hunt_variable[0]
            points = hunt_variable[1]
        elif choice == "3":
            from shop import loop_welcome
            while True:
                shop_variable = loop_welcome(gold, cheese, trap)
                gold = shop_variable[0]
                cheese = shop_variable[1]
                break
        elif choice == "4":
            arm_trap_cheese_name = change_cheese(player_name, trap, cheese)
            if arm_trap_cheese_name is None:
                continue
            arm_trap = arm_trap_cheese_name[0]
            if arm_trap is None:
                trap = "Cardboard and Hook Trap"
            cheese_name = arm_trap_cheese_name[1]


def main():
    q1.main()
    player_name = ye_name()
    train_or_not(player_name)


if __name__ == '__main__':
    main()
