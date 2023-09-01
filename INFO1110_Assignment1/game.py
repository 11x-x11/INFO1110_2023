'''
Answer for Question 7 - PIAT: The Hunt

Name: Shaoqing Ni
SID: 530532312
unikey: shni6293

'''

import random
import q1


def ye_name():
    name = input("\nWhat's ye name, Hunter?\n")
    from name import is_valid_name
    state = is_valid_name(name)
    if state is True:
        print(f'Welcome to the Kingdom, Hunter {name}!')
        return name
    else:
        print('Welcome to the Kingdom, Hunter Bob!')
        return "Bob"


def train_or_not(player_name):
    from train import main
    discussion = input('''Before we begin, let's train you up!
Press "Enter" to start training or "skip" to Start Game: ''')
    if discussion == '':
        print()
        trap = main()
        menu(player_name, trap)
    elif discussion == "skip":
        trap = "Cardboard and Hook Trap"
        menu(player_name, trap)


def hunt(gold=125, cheese=0, points=0):
    hunts_without_catch = 0
    exit_hunt = False
    while not exit_hunt:
        print("Sound the horn to call for the mouse...")
        choice = input('Sound the horn by typing "yes": ')
        if choice == "yes" and cheese >= 1:
            Random = random.random()
            if Random <= 0.5:
                print("Caught a Brown mouse!")
                gold += 125
                points += 115
                cheese -= 1
                hunts_without_catch = 0
                print(f"My gold: {gold}, My points: {points}\n")
            elif Random > 0.5:
                print("Nothing happens.")
                cheese -= 1
                hunts_without_catch += 1
                print(f"My gold: {gold}, My points: {points}\n")
            if hunts_without_catch >= 5:
                continue_choice = input("Do you want to continue to hunt? ")
                if continue_choice == "no":
                    exit_hunt = True
                elif continue_choice == "yes":
                    hunts_without_catch = 0
        elif choice == "yes" and cheese <= 0:
            print("Nothing happens. You are out of cheese!")
            hunts_without_catch += 1
            print(f"My gold: {gold}, My points: {points}\n")
            if hunts_without_catch >= 5:
                continue_choice = input("Do you want to continue to hunt? ")
                if continue_choice == "no":
                    exit_hunt = True
                elif continue_choice == "yes":
                    hunts_without_catch = 0
        elif choice == "stop hunt":
            exit_hunt = True
        else:
            print("Do nothing.")
            print(f"My gold: {gold}, My points: {points}\n")
            continue

    return (gold, cheese, points), exit_hunt


def menu(player_name, trap):
    Status = False
    gold_cheese = [125, 0]
    point = [0]
    while not Status:
        print(f'\nWhat do ye want to do now, Hunter {player_name}?', end="")
        choice = input('''
1. Exit game
2. Join the Hunt
3. The Cheese Shop\n''')
        if choice == "1":
            exit()
        elif choice == "2":
            exit_hunt = False
            while not exit_hunt:
                hunt_variable, exit_hunt = hunt(
                    gold_cheese[0], gold_cheese[1], point[0])
                gold_cheese = [hunt_variable[0], hunt_variable[1]]
                point = [hunt_variable[2]]
        elif choice == "3":
            from shop import loop_welcome
            exit_shop = False
            while not exit_shop:
                print('''Welcome to The Cheese Shop!
Cheddar - 10 gold''')
                shop_variable, exit_shop = loop_welcome(
                    gold_cheese[0], gold_cheese[1], trap)
                gold_cheese = [shop_variable[0], shop_variable[1]]


def main():
    q1
    player_name = ye_name()
    train_or_not(player_name)


if __name__ == '__main__':
    main()
