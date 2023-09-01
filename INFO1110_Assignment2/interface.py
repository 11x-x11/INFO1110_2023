'''
Write your solution for the class Interface here.
This is your answer for Question 8.4.

Author: Ni shaoqing
SID: 530532312
Unikey: shni6293
'''


import sys
from hunter import Hunter
from cshop import CheeseShop
import game_final
import game


class Interface:
    def __init__(self, menu={'1.': 'Exit game','2.': 'Join the Hunt', '3.': 'The Cheese Shop', '4.': 'Change Cheese'}, player= Hunter()):
        self.menu = menu
        self.player = player

    def set_player(self, player):
        if isinstance(player, Hunter):
            self.player = player

    def get_menu(self):
        list_menu = []
        list_index = 0
        while list_index < len(self.menu):
            list_menu.append(f'{list(self.menu)[list_index]} {self.menu[list(self.menu)[list_index]]}')
            list_index += 1
        return f'''{list_menu[0]}
{list_menu[1]}
{list_menu[2]}
{list_menu[3]}'''

    def change_cheese(self):
        name = self.player.name
        trap = str(self.player.trap)
        cheese = self.player.cheese
        e_flag = self.player.trap.one_time_enchantment
        status = game.change_cheese(name, trap, cheese, e_flag)
        self.player.trap.arm_status = status[0]
        self.player.trap.trap_cheese = status[1]

    def cheese_shop(self):
        shop = CheeseShop()
        shop.move_to(self.player)

    def hunt(self):
        gold = self.player.gold
        cheese_list = self.player.cheese
        trap_cheese = self.player.trap.trap_cheese
        point = self.player.points
        e_flag = self.player.trap.one_time_enchantment
        hunt_game = game_final.hunt(gold, cheese_list, trap_cheese, point, e_flag)
        self.player.gold = hunt_game[0]
        self.player.points = hunt_game[1]
        self.player.trap.one_time_enchantment = False

    def move_to(self, choice: int):
        while True:
            if isinstance(choice, int) is False:
                print('Invalid input. Try again!')
                break
            else:
                if choice < 1 or choice > 4:
                    print('Must be within 1 and 4.')
                    break
                elif choice == 1:
                    sys.exit(1)
                elif choice == 2:
                    self.hunt()
                    break
                elif choice == 3:
                    print(CheeseShop().greet())
                    print()
                    self.cheese_shop()
                    break
                elif choice == 4:
                    self.change_cheese()
                    break
