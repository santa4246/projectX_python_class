import json

def main():
    file_name = 'mission_computer_main.log'
    try:
        # 수행과제
        print_log(file_name)
        log_list = print_list(file_name)
        reverse_list(log_list)
        log_dict_list = list_to_dict(log_list)
        save_dict_to_jsonfile(log_dict_list)
        
        # 보너스과제
        search_text(log_dict_list)
        
    except IOError as err:
        print("I/O error: {0}".format(err))


def print_log(file_name):
    with open(file_name) as infile:
        for in_line in infile.readlines():
            print(in_line)

def print_list(file_name):
    log_list = []
    with open(file_name, 'r') as log_file:
        for line in log_file:
            log_items = line.strip().split(',')
            log_list.append(log_items)
        print(log_list)

    return log_list

def list_to_dict(log_list):
    log_dict_list = []
    for log_item in log_list:
        log_dict = {
            'timestamp': log_item[0],
            'event': log_item[1],
            'message': log_item[2]
        }
        log_dict_list.append(log_dict)

    print(log_dict_list)
    return log_dict_list

def reverse_list(log_list):
    print(log_list[::-1])

def save_dict_to_jsonfile(log_dict_list):
    with open('mission_computer_main.json', 'w') as json_file:
        json.dump(log_dict_list, json_file)

    print("mission_computer_main.json 파일이 업데이트되었습니다.")

def search_text(log_dict_list):
    search_string = 'noticeable'

    for log_dict in log_dict_list:
        found_keys = [key for key, value in log_dict.items() if search_string in value]
        if found_keys:
            print(f"'{search_string}'을(를) 포함한 키: {found_keys}")

if __name__ == "__main__":
    main()