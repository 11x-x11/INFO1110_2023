'''
Write your solution for the class CheeseShop here.
This is your answer for Question 8.3.

Author: Ni shaoqing
SID: 530532312
Unikey: shni6293
'''
from hunter import Hunter
import shop


class CheeseShop:
    # Initialize cheese shop with cheeses and menu
    def __init__(self) -> None:
        self.cheeses = {'Cheddar': 10, 'Marble': 50, 'Swiss': 100}
        self.menu = {'1.': 'Buy cheese', '2.': 'View inventory', '3.': 'Leave shop'}

    # Return a formatted string of available cheeses
    def get_cheeses(self):
        cheese_list = []
        list_of_cheese = list(self.cheeses)
        cheese_price_index = 0
        # Iterate over all available cheeses
        while cheese_price_index < len(list_of_cheese):
            cheese_list.append(f'{list_of_cheese[cheese_price_index]} - {self.cheeses[list_of_cheese[cheese_price_index]]} gold')
            cheese_price_index += 1
        return f'''{cheese_list[0]}
{cheese_list[1]}
{cheese_list[2]}'''

    # Returns a string representation of the menu options
    def get_menu(self):
        shop_menu = ''
        list_of_choice = list(self.menu)
        shop_menu_index = 0
        # Iterate over all menu options
        while shop_menu_index < len(list_of_choice):
            shop_menu += f'{list_of_choice[shop_menu_index]} {self.menu[list_of_choice[shop_menu_index]]}'
            if shop_menu_index < len(list_of_choice) - 1:
                shop_menu += '\n'
            shop_menu_index += 1
        return shop_menu

    # Returns a welcome message with the available cheeses
    def greet(self):
        return f'''Welcome to The Cheese Shop!
{self.get_cheeses()}'''

    # Buys cheese from the shop with the provided amount of gold
    def buy_cheese(self, gold: int):
        bought = list(shop.buy_cheese(gold))
        bought[0] = gold - bought[0]
        return tuple(bought)

    # a methods that can accept different actions during shopin
    def move_to(self, hunter: Hunter):
        while True:
            print('How can I help ye?')
            print(self.get_menu())
            choice = input()
            try:
                choice = int(choice)
            except ValueError:
                print('I did not understand.\n')
                continue
            if choice < 1 or choice > 3:
                raise ValueError('You should only choose between 1 and 3!')
            elif choice == 1:
                buy_cheese = self.buy_cheese(hunter.gold)
                hunter.gold = buy_cheese[0]
                hunter.update_cheese(buy_cheese[1])
            elif choice == 2:
                print(hunter.display_inventory())
            elif choice == 3:
                break
            else:
                print("I did not understand.")
            print()
