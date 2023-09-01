'''
Answer for Question 6 - PIAT: The Cheese Shop

Name: Shaoqing Ni
SID: 530531312
unikey: shni6293

'''


def buy_cheese(gold=125) -> tuple:
    cheddar = 10
    # Display available gold for the user
    print(f'You have {gold} gold to spend.')
    # Ask user to input the cheese name and quantity
    quantity = str(input('State [cheese quantity]: '))
    tuple_quantity = quantity.split(" ")
    # Varifey the user's input
    if len(quantity.split()) <= 2:
        if len(quantity.split()) == 2 and tuple_quantity[0].lower() == "cheddar":
            quantity = int(tuple_quantity[1])
            # calcualte the gold after purching
            gold = gold - int(quantity) * cheddar
            # check it user enter a positive quantity for buying cheese
            if quantity < 0:
                print('Must purchase a positive amount of cheese.')
                return (0, 0)
            # check if user have enough money to buy cheese
            if gold < 0:
                print("Insufficient gold.")
                return (0, 0)
            # Display the message of buying cheddar
            else:
                print(f'Successfully purchase {quantity} cheddar.')
                return ((int(quantity) * cheddar), int(quantity))
        # when user input back, than it go back to the menu
        elif quantity == "back":
            return (0, 0)
        # when user enter invalid command
        else:
            print("Sorry, did not understand.")
            return (0, 0)
    else:
        return (0, 0)


def display_inventory(gold: int = 125, cheese: int = None, trap="Cardboard and Hook Trap") -> None:
    # Display the current inventory
    print(f'''Gold - {gold}
Cheddar - {cheese}
Trap - {trap}''')


def choice():
    # Ask User to choose one of the options below to go further
    choice = int((input('''\nHow can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop
''')))
    return choice


def loop_welcome(gold, cheddar_num, trap="Cardboard and Hook Trap"):
    exit_shop = False
    # Loop until the user choose to exit(choose 3)
    while not exit_shop:
        Choice = choice()
        if Choice == 1:
            res = buy_cheese(gold)
            gold = gold - res[0]
            cheddar_num = cheddar_num + res[1]
        elif Choice == 2:
            display_inventory(gold=gold, cheese=cheddar_num, trap=trap)
        elif Choice == 3:
            exit_shop = True
    return (gold, cheddar_num), exit_shop


def main():
    cheddar_num = 0
    initial = 125
    # Display welcome message
    print('''Welcome to The Cheese Shop!
Cheddar - 10 gold''')
    loop_welcome(initial, cheddar_num)


if __name__ == '__main__':
    main()

