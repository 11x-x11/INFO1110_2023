'''
Write solutions to 4. New Mouse Release here.

Author: Ni shaoqing
SID: 530532312
Unikey: shni6293
'''
from mouse import generate_mouse


def test_generate_mouse():
    mouse_idx = 0
    mouse_list = []
    while mouse_idx < 10000:
        actual_random = generate_mouse()
        mouse_list.append(actual_random)
        mouse_idx += 1
    None_num = mouse_list.count(None)
    Brown_num = mouse_list.count("Brown")
    Field_num = mouse_list.count("Field")
    Grey_num = mouse_list.count("Grey")
    White_num = mouse_list.count("White")
    Tiny_num = mouse_list.count("Tiny")
    print(None_num)
    print(Brown_num)
    print(Field_num)
    print(Grey_num)
    print(White_num)
    print(Tiny_num)


if __name__ == '__main__':
    test_generate_mouse()
