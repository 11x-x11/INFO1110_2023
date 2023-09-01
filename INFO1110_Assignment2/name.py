'''
Answer for Question 5. Kids' Friendly.

Author: Ni Shaoqing
SID: 530532312
Unikey: shni6293

'''
import os


# Function that checks if the length of the name is between 1- 9 characters
def is_valid_length(name: str) -> bool:
    return 1 <= len(name) <= 9


# Function that checks if the name starts with an alphabet
def is_valid_start(name: str) -> bool:
    return len(name) != 0 and name[0].isalpha()


# Fnction that checks if the name is a single word
def is_one_word(name: str) -> bool:
    return len(name) != 0 and len(name.split()) == 1 and not (name[0].isspace() or name[-1].isspace())


# check if the argument word is a is_profanity word or not according to the given database
def is_profanity(word: str, database='/home/files/list.txt', records='/home/files/history.txt') -> bool:
    word = word.strip().lower()
    if os.path.isfile(database) is False:
        print('Check directory of database!')
        return False
    else:
        status = False
        with open(database, "r") as data:
            read_data = data.read().splitlines()
        i = 0
        while i < len(read_data):
            if word == read_data[i]:
                status = True
                break
            i += 1
        if status is True:
            if os.path.exists(records) is False or os.path.isfile(records) is False:
                with open(records, 'w') as create_record:
                    create_record.write('')
            if os.path.exists(records) and os.path.isfile(records):
                with open(records, "a") as reco:
                    reco.write(f'{word}\n')
                    return True
        else:
            return False


# count the time of appearence of the given argument "word" in the record file
def count_occurrence(word: str, file_records='/home/files/history.txt', start_flag=True) -> int:
    if isinstance(word, str) is False:
        print("First argument must be a string object!")
        return 0
    else:
        if len(word) == 0:
            print("Must have at least one character in the string!")
            return 0
        else:
            if word[0].isalpha() is False:
                print("First argument must be a string object!")
                return 0
    if os.path.exists(file_records) is False:
        print("File records not found!")
        return 0
    with open(file_records, 'r') as read_records:
        line = read_records.read().lower().splitlines()
        while True:
            if start_flag is True:
                first_letter_line = []
                i = 0
                while i < len(line):
                    first_letter_line.append(line[i][0])
                    i += 1
                count = first_letter_line.count(word.lower()[0])
                break
            else:
                count = line.count(word.lower())
                break
    return count


def is_valid_name_old(name: str) -> bool:
    return is_valid_length(name) and is_valid_start(name) and is_one_word(name)


# Function used to determine if the name is valid by checking all condtions.
def is_valid_name(name: str) -> bool:
    return is_profanity(name) is False and is_valid_name_old(name) is True


# Function used to generate a new name according to the given file
def generate_name(word: str, src="/home/files/animals.txt", past="/home/files/names.txt") -> str:
    if isinstance(word, str) is False or len(word) == 0 or word[0].isalpha() is False or not os.path.exists(src):
        if isinstance(word, str) is False:
            print("First argument must be a string object!")
        elif len(word) == 0 :
            print("Must have at least one character in the string!")
        elif word[0].isalpha() is False:
            print("First argument must be a string object!")
        elif not os.path.exists(src):
            print("Source file is not found!")
        with open(past, 'a') as append_Bob:
            append_Bob.write('Bob\n')
        return 'Bob'
    else:
        if os.path.exists(past) is False:
            with open(past, 'w') as write_new_past:
                write_new_past.write('')
        with open(src, 'r') as read_animal:
            animal_list = read_animal.read().strip().split()
        animal_dict = {}
        first_letters = []
        letter = ord('a')
        while letter <= ord('z'):
            first_letters.append(chr(letter))
            letter += 1
        key_index = 0
        while key_index < len(first_letters):
            letter_key = first_letters[key_index]
            animal_dict[letter_key] = []
            animal_idx = 0
            while animal_idx < len(animal_list):
                animal_name = animal_list[animal_idx].lower()
                if animal_name[0] == letter_key:
                    animal_dict[letter_key].append(animal_name)
                animal_idx += 1
            key_index += 1
        with open(past, 'r') as read_past:
            past_name_list = read_past.read().strip().split()
        first_letter_past = []
        past_idx = 0
        while past_idx < len(past_name_list):
            first_letter_past.append(past_name_list[past_idx][0])
            past_idx += 1
        word_1st = word.lower()[0]
        count_past = first_letter_past.count(word_1st)
        new_name = animal_dict[word_1st][count_past % len(animal_dict[word_1st])]
        with open(past, 'a') as append_name:
            append_name.write(new_name + '\n')
        return new_name


def main():
    while True:
        name = input("Check name: ").strip().lower()
        check_name = is_valid_name(name)
        if name == 's':
            break
        elif check_name is True:
            print(f"{name} is a valid name!")
        elif check_name is False:
            new_name = generate_name(name)
            print(f"Your new name is: {new_name}", end="\n")


if __name__ == "__main__":
    main()
