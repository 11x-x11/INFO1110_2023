'''
Write your solution for the class Trap here.
This is your answer for Question 8.1.

Author: Ni shaoqing
SID: 530532312
Unikey: shni6293
'''


class Trap:
    def __init__(self, trap_name='', trap_cheese=None, arm_status=False, one_time_enchantment=False) -> None:
        self.trap_name = trap_name
        self.trap_cheese = trap_cheese
        self.arm_status = arm_status
        self.one_time_enchantment = one_time_enchantment

    def set_trap_name(self, name):
        choice_of_trap_name = ('Cardboard and Hook Trap', 'High Strain Steel Trap', 'Hot Tub Trap')
        check_trap = 0
        while check_trap < len(choice_of_trap_name):
            if name == choice_of_trap_name[check_trap]:
                self.trap_name = choice_of_trap_name[check_trap]
                break
            check_trap += 1

    def set_trap_cheese(self, cheese: str):
        valid_trap_cheese = ('Cheddar', 'Marble', 'Swiss')
        check_cheese = 0
        self.trap_cheese = None
        while check_cheese < len(valid_trap_cheese):
            if cheese == valid_trap_cheese[check_cheese]:
                self.trap_cheese = valid_trap_cheese[check_cheese]
                break
            check_cheese += 1

    def set_arm_status(self):
        if self.trap_name == '' or self.trap_cheese is None:
            self.arm_status = False
        else:
            self.arm_status = True

    def set_one_time_enchantment(self, e_flag):
        if self.trap_name != 'Cardboard and Hook Trap':
            self.one_time_enchantment = e_flag
        else:
            self.one_time_enchantment = False

    def get_trap_name(self):
        return self.trap_name

    def get_trap_cheese(self):
        return self.trap_cheese

    def get_arm_status(self):
        return self.arm_status

    def get_one_time_enchantment(self):
        return self.one_time_enchantment

    @staticmethod
    def get_benefit(cheese):
        if cheese == "Cheddar":
            return "+25 points drop by next Brown mouse"
        elif cheese == "Marble":
            return "+25 gold drop by next Brown mouse"
        elif cheese == "Swiss":
            return "+0.25 attraction to Tiny mouse"

    def __str__(self) -> str:
        if self.one_time_enchantment is True:
            return f'One-time Enchanted {self.trap_name}'
        else:
            return self.trap_name
