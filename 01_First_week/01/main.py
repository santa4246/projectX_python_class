def main():
    file_name = 'mission_computer_main.log'

    # 수행과제
    print_hello()
    print_log(file_name)

    # 보너스과제
    print_log_reverse(file_name)
    save_err_log(file_name)

def print_hello():
    print('Hello Mars')

def print_log(file_name):
    try:
        with open(file_name) as infile :
            for in_line in infile.readlines():
                print(in_line)
    except IOError as err :
        print("I/O error: {0}".format(err))

def print_log_reverse(file_name):
    try:
        with open(file_name) as infile :
            for in_line in reversed(infile.readlines()):
                print(in_line)
    except IOError as err:
        print("I/O error: {0}".format(err))

def save_err_log(file_name):
    try:
        with open(file_name) as infile :
            f = open("problem.txt", 'w')
            for in_line in infile.readlines()[33:36]:
                f.write(in_line)
            f.close()
    except IOError as err:
        print("I/O error: {0}".format(err))

if __name__ == "__main__":
    main()