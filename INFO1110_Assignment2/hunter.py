'''
Write your solution for the class Hunter here.
This is your answer for Question 8.2.

Author: Ni shaoqing
SID: 530532312
Unikey: shni6293
'''

from trap import Trap
import name


class Hunter:
    def __init__(self, name="Bob", cheese=[["Cheddar", 0], ["Marble", 0], ["Swiss", 0]], trap=Trap(), gold=125, points=0) -> None:
        self.name = name
        self.cheese = cheese
        self.trap = trap
        self.gold = gold
        self.points = points

    def set_name(self, player_name):
        if name.is_valid_name(player_name) is True and name.is_profanity(player_name) is False:
            self.name = player_name
        else:
            self.name = 'Bob'

    def set_cheese(self, cheese_num_tuple):
        if isinstance(cheese_num_tuple, tuple):
            update_index = 0
            while update_index < len(cheese_num_tuple):
                self.cheese[update_index][1] = cheese_num_tuple[update_index]
                update_index += 1

    def set_gold(self, gold):
        if isinstance(gold, int):
            self.gold = gold

    def set_points(self, points):
        if isinstance(points, int):
            self.points = points

    def get_name(self):
        return self.name

    def get_cheese(self):
        return f'''{self.cheese[0][0]} - {self.cheese[0][1]}
{self.cheese[1][0]} - {self.cheese[1][1]}
{self.cheese[2][0]} - {self.cheese[2][1]}'''

    def get_gold(self):
        return self.gold

    def get_points(self):
        return self.points

    def update_cheese(self, cheese_tuple: tuple):
        if isinstance(cheese_tuple, tuple) is True:
            update_index = 0
            while update_index < len(cheese_tuple):
                self.cheese[update_index][1] += cheese_tuple[update_index]
                update_index += 1

    def consume_cheese(self, cheese_type: str):
        check_exist = 0
        while check_exist < len(self.cheese):
            if cheese_type == self.cheese[check_exist][0]:
                self.cheese[check_exist][1] -= 1
            check_exist += 1

    def have_cheese(self, cheese_type='Cheddar'):
        if not isinstance(cheese_type, str):
            return 0
        check_exist = 0
        while check_exist < len(self.cheese):
            if cheese_type.lower().capitalize() == self.cheese[check_exist][0]:
                return self.cheese[check_exist][1]
            check_exist += 1
        return 0

    def display_inventory(self):
        return f'''Gold - {self.gold}
{self.cheese[0][0]} - {self.cheese[0][1]}
{self.cheese[1][0]} - {self.cheese[1][1]}
{self.cheese[2][0]} - {self.cheese[2][1]}
Trap - {str(self.trap)}'''

    def arm_trap(self, arm_trap: str):
        arm_trap = arm_trap.lower().capitalize()
        if self.have_cheese(cheese_type=arm_trap) > 0:
            self.trap.set_trap_cheese(arm_trap)
        else:
            self.trap.trap_cheese = None
        self.trap.set_arm_status()

    def update_gold(self, gold: int):
        if isinstance(gold, int) is True:
            self.gold += gold

    def update_points(self, points: int):
        if isinstance(points, int) is True:
            self.points += points

    def __str__(self) -> str:
        return f'''Hunter {self.name}
{self.display_inventory()}'''
