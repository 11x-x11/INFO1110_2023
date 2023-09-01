'''
Answer for Question 3 - Function

Name: Shaoqing Ni
SID: 530532312
unikey: shni6293

'''


# Function that checks if the length of the name is between 1- 9 characters
def is_valid_length(name: str) -> bool:
    return 1 <= len(name) <= 9


# Function that checks if the name starts with an alphabet
def is_valid_start(name: str) -> bool:
    return len(name) != 0 and name[0].isalpha()


# Fnction that checks if the name is a single word
def is_one_word(name: str) -> bool:
    return len(name) != 0 and len(name.split()) == 1 and not (name[0].isspace() or name[-1].isspace())


# Function used to determine if the name is valid by checking all condtions.
def is_valid_name(name: str) -> bool:
    return is_valid_length(name) is True and is_valid_start(name) is True and is_one_word(name) is True
