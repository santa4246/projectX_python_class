def main():
    file_name = 'mission_computer_main.log'
    try:
        print_hello()
        print_log(file_name)

        print_log_reverse(file_name)
        save_err_log(file_name)

    except IOError as err :
        print("error: {0}".format(err))

def print_hello():
    print('Hello Mars')

def print_log(file_name):
    with open(file_name) as infile :
        for in_line in infile.readlines():
            print(in_line)

def print_log_reverse(file_name):
    with open(file_name) as infile :
        for in_line in reversed(infile.readlines()):
            print(in_line)

def save_err_log(file_name):
    with open(file_name) as infile :
        f = open("problem.txt", 'w')
        for in_line in infile.readlines()[33:36]:
            f.write(in_line)
        f.close()

if __name__ == "__main__":
    main()