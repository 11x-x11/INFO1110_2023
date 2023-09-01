test_diro = "/home/test_file/"


def test_buy_cheese():
    with open(test_diro + 'buy_cheese.out', 'r') as read_act, open(test_diro + 'test_buy_cheese.expect', 'r') as read_expe:
        read_idx = 1
        actual = read_act.readline()
        expect = read_expe.readline()
        while actual or expect:
            assert actual == expect, f'\nYou fail at line {read_idx}\nExpectd: {expect} \nActual: {actual}'
            actual = read_act.readline()
            expect = read_expe.readline()
            read_idx += 1
        print("Congratualtions! You have successfully pass all test cases for buy_cheese function!")


def test_change_cheese():
    with open(test_diro + 'change_cheese.out', 'r') as read_act, open(test_diro + 'test_change_cheese.expect', 'r') as read_expe:
        read_idx = 1
        actual = read_act.readline()
        expect = read_expe.readline()
        while actual or expect:
            assert actual == expect, f'\nYou fail at line {read_idx}\nExpectd: {expect} \nActual: {actual}'
            actual = read_act.readline()
            expect = read_expe.readline()
            read_idx += 1
        print("Congratualtions! You have successfully pass all test cases for change_cheese function!")


def main():
    test_buy_cheese()
    test_change_cheese()


if __name__ == "__main__":
    main()
