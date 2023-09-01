'''
Write your solution for 6. PIAT: Check Setup here.

Author: Ni shaoqing
SID: 530521312
Unikey: shni6293
'''
import os
import shutil
import sys
from datetime import datetime


# Function to get the current time
def current_date():
    now = datetime.now()
    local_date_time = now.strftime("%d %b %Y %H:%M:%S")
    return local_date_time


# function to log the list of string into relvant log file
def logging(logs: list, date: str, time: str) -> None:
    current_diro = os.getcwd()
    folder_path = f'{current_diro}/logs/{date}'
    if os.path.exists(folder_path) is False:
        os.makedirs(folder_path)
    log_file = f'{folder_path}/{time}.txt'
    writing_index = 0
    with open(log_file, 'w') as write_file:
        while writing_index < len(logs):
            write_file.write(logs[writing_index] + "\n")
            writing_index += 1


# function to verify if all file is correct set up
def verification(master: str, timestamp: str) -> list:
    output = []
    output.append(f'{timestamp} Start verification process.')
    output.append(f'{timestamp} Extracting paths in configuration file.')
    config_path = os.path.join(master, 'config.txt')
    with open(config_path, 'r') as read_config:
        config_file, path_dict = {}, {}
        path_dict['file_path'], path_dict['master_path'] = [], []
        current_key = None
        config = read_config.readline().strip()
        while config:
            if config.startswith('/') and config.endswith('/'):
                current_key = config
                config_file[current_key] = []
            elif current_key is not None and config.startswith('./'):
                config_file[current_key].append(config)
                path_dict['file_path'].append(os.path.join(current_key, config.lstrip("./")))
                folder_name = os.path.basename(current_key.rstrip('/'))
                file_path = os.path.join(master, os.path.basename(folder_name), config.lstrip("./"))
                path_dict['master_path'].append(file_path)
            config = read_config.readline().strip()
    output.append(f'Total directories to check: {len(config_file)}')
    output.append(f'{timestamp} Checking if directories exists.')
    folder_index = 0
    while folder_index < len(config_file):
        config_keys = tuple(config_file.keys())
        if os.path.exists(config_keys[folder_index]):
            output.append(f'{config_keys[folder_index]} is found!')
        else:
            output.append(f'{config_keys[folder_index]} NOT found!')
            output.append("Abnormalities detected...")
            return output
        folder_index += 1
    output.append(f'{timestamp} Extracting files in configuration file.')
    file_idx = 0
    while file_idx < len(path_dict['file_path']):
        output.append(f"File to check: {path_dict['file_path'][file_idx]}")
        file_idx += 1
    output.append(f"Total files to check: {len(path_dict['file_path'])}")
    output.append(f'{timestamp} Checking if files exists.')
    exist_idx = 0
    while exist_idx < len(path_dict['file_path']):
        if os.path.exists(path_dict['file_path'][exist_idx]):
            output.append(f"{path_dict['file_path'][exist_idx]} found!")
        else:
            output.append(f"{path_dict['file_path'][exist_idx]} NOT found!")
            return output
        exist_idx += 1
    output.append(f'{timestamp} Check contents with master copy.')
    file_read_idx = 0
    while file_read_idx < len(path_dict['file_path']):
        actual_file = path_dict['file_path'][file_read_idx]
        master_file = path_dict['master_path'][file_read_idx]
        actual_list, master_list = [], []
        with open(actual_file) as read_actual, open(master_file) as read_master:
            actual_read = read_actual.readline().strip()
            master_read = read_master.readline().strip()
            read_idx = 0
            while actual_read or master_read:
                actual_list.append(actual_read)
                master_list.append(master_read)
                read_idx += 1
                if actual_read != master_read:
                    print_idx = 0
                    while True:
                        if print_idx < read_idx:
                            output.append(f"File name: {actual_file}, {actual_list[print_idx]}, {master_list[print_idx]}")
                            print_idx += 1
                        elif print_idx == read_idx:
                            output.append('Abnormalities detected...')
                            return output
                actual_read = read_actual.readline().strip()
                master_read = read_master.readline().strip()
        output.append(f'{actual_file} is same as {master_file}: True')
        file_read_idx += 1
    output.append(f'{timestamp}  Verification complete.')
    return output


# functions to install the relvant file according to the given master directory
def installation(master: str, timestamp: str) -> list:
    output = []
    output.append(f'{timestamp} Start installation process.')
    output.append(f'{timestamp} Extracting paths in configuration file.')
    config_path = os.path.join(master, 'config.txt')
    with open(config_path, 'r') as read_config:
        config_file, path_dict = {}, {}
        path_dict['file_path'], path_dict['all_file_master'], path_dict['master_path'] = [], [], []
        current_key = None
        config = read_config.readline().strip()
        while config:
            if config.startswith('/') and config.endswith('/'):
                current_key = config
                config_file[current_key] = []
            elif current_key is not None and config.startswith('./'):
                config_file[current_key].append(config)
                path_dict['file_path'].append(os.path.join(current_key, config.lstrip("./")))
                folder_name = os.path.basename(current_key.rstrip('/'))
                file_path = os.path.join(master, os.path.basename(folder_name), config.lstrip("./"))
                path_dict['master_path'].append(file_path)
            config = read_config.readline().strip()
    output.append(f'Total directories to create: {len(config_file)}')
    output.append(f'{timestamp} Create new directories.')
    folder_index = 0
    while folder_index < len(config_file):
        config_keys = tuple(config_file.keys())
        if os.path.exists(config_keys[folder_index]):
            output.append(f'{config_keys[folder_index]} exists. Skip directory creation.')
        else:
            os.mkdir(config_keys[folder_index])
            output.append(f'{config_keys[folder_index]} is created successfully.')
        folder_index += 1
    output.append(f'{timestamp} Extracting paths of all files in {master}.')
    top_level_directories = sorted(next(os.walk(master))[1])
    dir_idx = 0
    count_index = 0
    while dir_idx < len(top_level_directories):
        dir_path = os.path.join(master, top_level_directories[dir_idx])
        walk_gen = os.walk(dir_path)
        try:
            sub_root, sub_directories, sub_files = next(walk_gen)
            sub_files = sorted(sub_files)
            file_idx = 0
            while file_idx < len(sub_files):
                file = sub_files[file_idx]
                file_path = os.path.join(sub_root, file)
                output.append(f"Found: {file_path}")
                path_dict['all_file_master'].append(sub_files[file_idx])
                file_idx += 1
                count_index += 1
        except StopIteration:
            pass
        dir_idx += 1
    output.append(f'{timestamp}  Create new files.')
    create_index = 0
    while create_index < len(list(path_dict['file_path'])):
        with open(list(path_dict['file_path'])[create_index], 'w') as creat_file:
            creat_file.write('')
        output.append(f"Creating file: {list(path_dict['file_path'])[create_index]}")
        create_index += 1
    output.append(f'{timestamp} Copying files.')
    copy_index = 0
    while copy_index < len(path_dict['file_path']):
        origianl = path_dict['master_path'][copy_index]
        destination = path_dict['file_path'][copy_index]
        output.append(f"Locating: {path_dict['all_file_master'][copy_index]}")
        if os.path.exists(origianl) is False or os.path.exists(destination) is False:
            if os.path.exists(origianl) is False:
                output.append(f"Original path: {origianl} is not found.")
            else:
                output.append(f"Original path: {destination} is not found.")
            output.append('Installation error...')
            return output
        else:
            shutil.copy2(origianl, destination)
            output.append(f"Original path: {origianl}")
            output.append(f"Destination path: {destination}")
        copy_index += 1
    output.append(f'{timestamp}  Installation complete.')
    return output


# main program and also check if the flags are correct or not
def main(master: str, flags: str, timestamp: str):
    now = datetime.strptime(timestamp, "%d %b %Y %H:%M:%S")
    date = now.strftime("%Y-%b-%d")
    time = now.strftime("%H_%M_%S")
    error_messages = {
        'Inva_master_diro': 'Invalid master directory.',
        'only_log': 'Invalid flag. Log can only run with install or verify.',
        'both_verify_install': 'Invalid flag. Choose verify or install process not both.',
        'same_character': 'Invalid flag. Each character must be unique.',
        'command_otherthan_i_v_l': "Invalid flag. Character must be a combination of 'v' or 'i' and 'l'.",
        'start_with_-': "Invalid flag. Flag must start with '-'."}
    if os.path.exists(master) is False:
        sys.stderr.write(f"{error_messages['Inva_master_diro']}\n")
    elif flags.startswith('-'):
        flags = flags[1:]
        flags = flags.lower()
        count_i = flags.count("i")
        count_v = flags.count("v")
        count_l = flags.count("l")
        count_other = len(flags) - count_i - count_v - count_l
        if count_l == 1 and count_i == 0 and count_v == 0:
            if count_other == 0:
                sys.stderr.write(f"{error_messages['only_log']}\n")
            elif count_other > 0:
                sys.stderr.write(f"{error_messages['command_otherthan_i_v_l']}\n")
        elif count_i == count_v == 1:
            if count_other > 0:
                sys.stderr.write(f"{error_messages['command_otherthan_i_v_l']}\n")
            else:
                sys.stderr.write(f"{error_messages['both_verify_install']}\n")
        elif count_i == 1 or count_v == 1:
            if count_other == 0 and count_v == 0:
                output = installation(master, timestamp)
                output_index = 0
                while output_index < len(output):
                    print(output[output_index])
                    output_index += 1
            elif count_other == 0 and count_i == 0:
                output = verification(master, timestamp)
                output_index = 0
                while output_index < len(output):
                    print(output[output_index])
                    output_index += 1
            elif count_i > 1 or count_v > 1:
                sys.stderr.write(f"{error_messages['same_character']}\n")
            else:
                sys.stderr.write(f"{error_messages['command_otherthan_i_v_l']}\n")
            if count_l == 1:
                logging(output, date, time)
        elif count_l > 1 or count_v > 1 or count_i > 1:
            sys.stderr.write(f"{error_messages['same_character']}\n")
        elif count_other > 0:
            sys.stderr.write(f"{error_messages['command_otherthan_i_v_l']}\n")
    elif flags.startswith('-') is False:
        sys.stderr.write(f"{error_messages['start_with_-']}\n")


# check the commanlind arguments and pass the default value
if __name__ == "__main__":
    try:
        abs_path = sys.argv[1]
        try:
            flag = sys.argv[2]
        except IndexError:
            flag = '-il'
        local_time = current_date()
        main(master=abs_path, flags=flag, timestamp=local_time)
    except IndexError:
        sys.stderr.write('Insufficient arguments.\n')
