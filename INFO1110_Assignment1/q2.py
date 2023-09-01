'''
Answer for Question 2 - What's ye called?

Name: Shaoqing Ni 
SID: 530532312 
unikey: shni6293

'''


# Print the initial question
print("Larry: What's ye name, Hunter?")

# Get user input for the name
name = input()

# Print the name confirmation question
print(f"Larry: Is '{name}' a name I can pronounce?")

# Check if the name length is valid (between 1 and 9 characters)
is_valid_length = 1 <= len(name) <= 9
print(
    f'It has a length of {len(name)} which is between 1 to 9 characters? {is_valid_length}!')

# Check if the name starts with an alphabet
is_valid_start = len(name) != 0 and name[0].isalpha()
print(f'It starts with an alphabet? {is_valid_start}')

# Check if the name is a single word
is_one_word = len(name) != 0 and len(name.split()) == 1 and not (
    name[0].isspace() or name[-1].isspace())
print(f'It is a single word? {is_one_word}')

# Determine if the name is valid by checking three conditions listed above
is_valid_name = is_valid_length and is_valid_start and is_one_word
print(f'Larry: I can pronounce this name --- {is_valid_name}')
