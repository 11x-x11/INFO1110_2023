from game import change_cheese


def test_positive_test():
    expect_output = (True, 'Cheddar')
    actual_output = change_cheese("Steven", "Cardboard and Hook Trap", [['Cheddar', 1], ["Marble", 0], ["Swiss", 0]])
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    expect_output = (True, "Marble")
    actual_output = change_cheese("Bob", "Test only trap", [['Cheddar', 1], ["Marble", 2], ["Swiss", 0]])
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'


def test_negative_test():
    expect_output = (False, None)
    actual_output = change_cheese("Jack Li", "Hot Tub Trap", [['Cheddar', 0], ["Marble", 0], ["Swiss", 0]])
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    expect_output = (False, None)
    actual_output = change_cheese("Henry", "High Strain Steel Trap", [['Cheddar', 2], ["Marble", 0], ["Swiss", 1]])
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'


def test_edge_test():
    expect_output = (False, None)
    actual_output = change_cheese("Steven", "Cardboard and Hook Trap", [])
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'
    expect_output = (False, None)
    actual_output = change_cheese("Steven", "Cardboard and Hook Trap", [['Cheddar', 0], ["Marble", 0], ["Swiss", 0]])
    assert actual_output == expect_output, f'\nReturn Value: \nActual: {actual_output} \nExpect: {expect_output}'


test_positive_test()
test_negative_test()
test_edge_test()
print('\n\n\nYou have successfully pass all test cases!')
