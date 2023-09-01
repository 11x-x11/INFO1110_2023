'''
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author: Ni Shaoqing
SID: 530532312
Unikey: shni6293
'''

CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))


def welcome_menu():
    print('Welcome to The Cheese Shop!')
    t = 0
    while t <= 2:
        cheddar = (CHEESE_MENU[t][0], CHEESE_MENU[t][1])
        print(f'{cheddar[0]} - {cheddar[1]} gold')
        t += 1


def buy_cheese(gold: int) -> tuple:
    gold_spent = 0
    cheese_bought = [0, 0, 0]
    while True:
        print(f'You have {gold} gold to spend.')
        user_input = str(input('State [cheese quantity]: ')).strip().lower()
        split_input = user_input.split()
        if user_input == "back":
            break
        elif len(split_input) <= 2 and len(split_input) > 0:
            cheese_idx = 0
            found_cheese = False
            while cheese_idx < len(CHEESE_MENU):
                if split_input[0] == CHEESE_MENU[cheese_idx][0].lower():
                    found_cheese = True
                    cheese_name = CHEESE_MENU[cheese_idx][0]
                    cheese_price = CHEESE_MENU[cheese_idx][1]
                    break
                cheese_idx += 1
            if len(split_input) == 2:
                if found_cheese is True:
                    cheese_num = split_input[1].lstrip('-')
                    if cheese_num.isdigit():
                        cheese_quantity = int(split_input[1])
                        cost = cheese_quantity * cheese_price
                        if cheese_quantity <= 0:
                            print('Must purchase positive amount of cheese.')
                        elif gold - cost < 0:
                            print("Insufficient gold.")
                        else:
                            gold -= cost
                            print(f'Successfully purchase {cheese_quantity} {cheese_name.lower()}.')
                            gold_spent = gold_spent + cost
                            cheese_bought[cheese_idx] += cheese_quantity
                    else:
                        print("Invalid quantity.")
                        continue
                elif found_cheese is False:
                    print(f"We don't sell {split_input[0]}!")
                    continue
            elif len(split_input) == 1:
                if found_cheese is True:
                    print("Missing quantity.")
                    continue
                elif found_cheese is False:
                    print(f"We don't sell {user_input}!")
                    continue
        elif len(split_input) == 0:
            print(f"We don't sell {user_input}!")
            continue
        else:
            print("Sorry, did not understand.")
    return gold_spent, tuple(cheese_bought)


def display_inventory(gold: int, cheese: list, trap: str) -> None:
    print(f'Gold - {gold}')
    i = 0
    while i < len(cheese):
        print(f'{cheese[i][0]} - {cheese[i][1]}')
        i += 1
    print(f'Trap - {trap}')


def loop_welcome(gold, cheese, trap):
    welcome_menu()
    while True:
        print('''\nHow can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop
''', end='')
        choice = input()   
        if choice == '1':
            res = buy_cheese(gold)
            gold -= res[0]
            i = 0
            while i < len(cheese):
                cheese[i][1] += res[1][i]
                i += 1
        elif choice == '2':
            display_inventory(gold=gold, cheese=cheese, trap=trap)
        elif choice == '3':
            break
        else:
            print("I did not understand.")
    return gold, cheese, trap


def main():
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap = 'Cardboard and Hook Trap'
    loop_welcome(gold, cheese, trap)


if __name__ == "__main__":
    main()
