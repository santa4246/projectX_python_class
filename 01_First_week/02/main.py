def main():
    file_name = 'mission_computer_main.log'

    # 수행과제
    print_log(file_name)
    log_list = print_list(file_name)
    list_to_dict(log_list)
    reverse_list(log_list)
    
    # 보너스과제


def print_log(file_name):
    try:
        with open(file_name) as infile:
            for in_line in infile.readlines():
                pass
                # print(in_line)
    except IOError as err:
        print("I/O error: {0}".format(err))

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
            'key1': log_item[0],
            'key2': log_item[1],
            'key3': log_item[2]
        }
        log_dict_list.append(log_dict)

    print(log_dict_list)

def reverse_list(log_list):
    print(log_list[::-1])

if __name__ == "__main__":
    main()