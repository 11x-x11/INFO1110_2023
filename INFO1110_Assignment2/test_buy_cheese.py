from shop import buy_cheese


def test_positive_test():
    expect_output = (50, (5, 0, 0))
    actual_output = buy_cheese(125)
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    print()
    expect_output = (90, (4, 1, 0))
    actual_output = buy_cheese(125)
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    print()


def test_negative_test():
    expect_output = (0, (0, 0, 0))
    actual_output = buy_cheese(125)
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    print()
    expect_output = (0, (0, 0, 0))
    actual_output = buy_cheese(125)
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    print()
    expect_output = (0, (0, 0, 0))
    actual_output = buy_cheese(125)
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    print()


def test_edge_test():
    expect_output = (0, (0, 0, 0))
    actual_output = buy_cheese(125)
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    print()
    expect_output = (0, (0, 0, 0))
    actual_output = buy_cheese(0)
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    print()
    expect_output = (200, (0, 0, 2))
    actual_output = buy_cheese(200)
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    print()

test_positive_test()
test_negative_test()
test_edge_test()
print('\n\n\nYou have successfully pass all test cases!')
