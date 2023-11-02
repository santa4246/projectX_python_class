# 수행과제 1
# 파이썬 설치 확인을 위한 'Hello Mars' 출력
print('Hello Mars')

# 수행과제 2
# mission_computer_main.log 파일을 열고 전체 내용 출력
# 파일 처리 과정 예외처리 기능 추가
print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
file_name = 'mission_computer_main.log'
try:
    with open(file_name) as infile :
        for in_line in infile.readlines():
            print(in_line)
except IOError as err:
    print("I/O error: {0}".format(err))

print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
# 보너스과제 1
# 역순으로 정렬해서 출력
try:
    with open(file_name) as infile :
        for in_line in reversed(infile.readlines()):
            print(in_line)
except IOError as err:
    print("I/O error: {0}".format(err))

print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
# 보너스과제2
# 출력 결과 중 문제가 되는 부분만 따로 파일로 저장
try:
    with open(file_name) as infile :
        f = open("problem.txt", 'w')
        for in_line in infile.readlines()[33:36]:
            f.write(in_line)
        f.close()
except IOError as err:
    print("I/O error: {0}".format(err))