'''
Write solutions to 3. New Mouse Release here.

Author: Ni Shaoqing
SID: 530532312
Unikey: shni6293
'''


import random
import art


TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")


def generate_probabilities(cheese_type, enchant=False):
    if cheese_type == "Cheddar":
        return (0.5, 0.1, 0.15, 0.1, 0.1, 0.05)
    elif cheese_type == "Marble":
        return (0.6, 0.05, 0.2, 0.05, 0.02, 0.08)
    elif cheese_type == "Swiss":
        if enchant is False:
            return (0.7, 0.01, 0.05, 0.05, 0.04, 0.15)
        elif enchant is True:
            return (0.45, 0.01, 0.05, 0.05, 0.04, 0.4)


def generate_mouse(cheese='Cheddar', enchant=False) -> str | None:
    random_num = random.random()
    mouse_proba = generate_probabilities(cheese, enchant)
    proba_sum = []
    initial_prob = 0
    i = 0
    while i < len(mouse_proba):
        sum_of_proba = initial_prob + mouse_proba[i]
        proba_sum.append(sum_of_proba)
        initial_prob = sum_of_proba
        i += 1
    if random_num < proba_sum[0]:
        mouse_type = TYPE_OF_MOUSE[0]
    elif proba_sum[0] <= random_num < proba_sum[1]:
        mouse_type = TYPE_OF_MOUSE[1]
    elif proba_sum[1] <= random_num < proba_sum[2]:
        mouse_type = TYPE_OF_MOUSE[2]
    elif proba_sum[2] <= random_num < proba_sum[3]:
        mouse_type = TYPE_OF_MOUSE[3]
    elif proba_sum[3] <= random_num < proba_sum[4]:
        mouse_type = TYPE_OF_MOUSE[4]
    elif proba_sum[4] <= random_num < proba_sum[5]:
        mouse_type = TYPE_OF_MOUSE[5]
    return mouse_type


def loot_lut(mouse_type: str | None) -> tuple:
    if mouse_type == TYPE_OF_MOUSE[0]:
        gold = 0
        points = 0
    elif mouse_type == TYPE_OF_MOUSE[1]:
        gold = 125
        points = 115
    elif mouse_type == TYPE_OF_MOUSE[2]:
        gold = 200
        points = 200
    elif mouse_type == TYPE_OF_MOUSE[3]:
        gold = 125
        points = 90
    elif mouse_type == TYPE_OF_MOUSE[4]:
        gold = 100
        points = 70
    elif mouse_type == TYPE_OF_MOUSE[5]:
        gold = 900
        points = 200
    return gold, points


def generate_coat(type_of_mouse):
    if type_of_mouse == 'Brown':
        return art.BROWN
    elif type_of_mouse == 'Field':
        return art.FIELD
    elif type_of_mouse == "Grey":
        return art.GREY
    elif type_of_mouse == "White":
        return art.WHITE
    elif type_of_mouse == "Tiny":
        return art.TINY


class Mouse:
    def __init__(self, cheese="Cheddar", enchant=False):
        self.name = generate_mouse(cheese, enchant)
        self.gold, self.points = loot_lut(self.name)
        self.coat = generate_coat(self.name)

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold

    def get_points(self) -> int:
        return self.points

    def get_coat(self) -> str:
        return self.coat

    def __str__(self) -> str:
        if self.name:
            return self.name
        else:
            return "None"
