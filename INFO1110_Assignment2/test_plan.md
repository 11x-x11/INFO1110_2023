Author: Ni Shaoqing 
SID: 530532312
Unikey: shni6293



**Test Cases**
Table 1. Summary of test cases for `buy_cheese` function in `shop.py`. 

| Test ID | Description                                           | Inputs                                                                      | Expected Output                                                                                                                               | Status |
| ------- | ----------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 01      | Positive Test Cases - Buying Valid number of cheese   | gold: 125    ched_and_quant : "Cheddar 5", "back"                           | Successfully purchase 5 cheddar.                                                                          returned value: (50, (5, 0, 0))     | Pass   |
| 02      | Positive Test Cases - Buying Multiple Types of cheese | gold: 125    ched_and_quant: "Cheddar 1 ", "Marble 1", "Cheddar 3", "Back"  | Successfully purchase 1 cheddar. Successfully purchase 1 marble. Successfully purchase 3 cheddar.         returned value: (90, (4,1, 0))      | Pass   |
| 03      | Negative Test Cases -  Enter Invalid cheese number    | gold: 125    ched_and_quant: "cheddar -2", "back"                           | Error Message - "Must purchase a positive amount of cheese."                                              returned value: (0, (0, 0, 0))      | Pass   |
| 04      | Negative Test Cases - Enter empty quantity of cheese  | gold: 125    ched_and_quant: "cheddar", "back"                              | Error Message - "Missing quantity"                                                                        returned value: (0, (0,  0, 0))     | Pass   |
| 05      | Negative Test Cases - Insufficient gold               | gold: 125    ched_and_quant: "Swiss 2", "back"                              | Error Message - "Insufficient gold."                                                                      returned value: (0, (0, 0, 0))      | Pass   |
| 06      | Edge Test Cases - Enter empty String                  | gold: 125    ched_and_quant: "", "back"                                     | Error Message - "We don't sell !"                                                                         returned value: (0, (0, 0, 0))      | Pass   |
| 07      | Edge Test Cases - let gold be 0                       | gold: 0      ched_and_quant: "Cheddar 1", "back"                            | Error Message - "Insufficient gold."                                                                      returned value: (0, (0, 0, 0))      | Pass   |
| 08      | Edge Test Cases - Spend all the money to buy cheese   | gold: 200    ched_and_quant:"Swiss 2", "back"                               | Successfully purchase 2 Swiss.                                                                            returned value: (200, (0, 0, 2))    | Pass   |




Table 2. Summary of test cases for `change_cheese` function in `game.py`.

| Test ID | Description                                                 | Inputs                                                                                                                                                                         | Expected Output | Status |
| ------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ------ |
| 01      | Positive_test -- Valid Cheese Selection with spaces         | name="Steven",    trap = "Cardboard and Hook Trap",   cheese = [['Cheddar', 1], ["Marble", 0], ["Swiss", 0]]           e_flag = False      User's input: "    cheddar ", "yes" | True, Cheddar   | Pass   |
| 02      | Positive_test --  Valid Cheese Selection(Case_Insensitive)  | name="Bob",       trap = "Test only trap",            cheese = [['Cheddar', 1], ["Marble", 2], ["Swiss", 0]]           e_flag = False      User's input: "MarBLe", "   Yes  "  | True, Marble    | Pass   |
| 03      | Negative_test --  Invalid Cheese Selection                  | name="Jack Li",   trap = "Hot Tub Trapp",             cheese = [['Cheddar', 0], ["Marble", 0], ["Swiss", 0]]           e_flag = False      User's input: "Whatever", "back"    | False, None     | Pass   |
| 04      | Negative_test -- Out of Cheese                              | name="Henry",     trap = "High Strain Steel Trap",    cheese = [['Cheddar', 2], ["Marble", 0], ["Swiss", 1]]           e_flag = False      User's input: "Marble", "back"      | False, None     | Pass   |
| 05      | Edge_test -- empty cheese list                              | name="Steven",    trap = "Cardboard and Hook Trap",   cheese = []                                                      e_flag = False      User's input: "Marble", "back"      | False, None     | Pass   |
| 06      | Edge_test -- empty user impurt                              | name="Steven",    trap = "Cardboard and Hook Trap",   cheese = [['Cheddar', 0], ["Marble", 0], ["Swiss", 0]]           e_flag = False      User's input: ", "back"             | False, None     | Pass   |
