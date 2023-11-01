file_name = 'mission_computer_main.log' # 로그파일 이름 정의

try: # 파일 읽기 예외처리
    with open(file_name) as infile :
        for in_line in infile.readlines():
            print(in_line)
except IOError as err: # 에러 발생 시 출력
    print("I/O error: {0}".format(err))