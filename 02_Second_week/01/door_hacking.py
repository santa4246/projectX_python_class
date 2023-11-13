# 2-1 비밀번호 xxxxxx
import time
import zipfile

# 2-1-(2) 암호를 푸는 코드를 unlock_zip() 이라는 이름으로 함수로 만듦
def unlock_zip(file,password_length,password_list,password_file):
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with zipfile.ZipFile(file,'r') as zip_file:
        count = 0
        found_password = None
        characters = password_list
        for i in range(len(characters)):
            for j in range(len(characters)):
                for k in range(len(characters)):
                    for l in range(len(characters)):
                        for m in range(len(characters)):
                            for n in range(len(characters)):
                                password = characters[i] + characters[j] + characters[k] + characters[l] + characters[m] + characters[n]
                                try:
                                    zip_file.extractall(pwd=password.encode('utf-8'))
                                    found_password = password
                                    break
                                except Exception:
                                    count += 1
                                    print(f'반복 횟수 : {count}, 시도 패스워드 : {password}')
                            if found_password:
                                break
                        if found_password:
                            break
                    if found_password:
                        break
                if found_password:
                    break
            if found_password:
                break
    
    # 2-1-(3) 암호를 푸는 과정을 출력하는데 시작 시간과 반복 회수 그리고 진행 시간등을 출력
    found_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    elapsed_time = round(time.time() - time.mktime(time.localtime()),3)

    print(f'시작시간 : {start_time}')
    print(f'끝나는 시간 : {found_time}')
    print(f'걸린 시간: {elapsed_time} 초')
    
    with open(password_file,'w') as f:
        f.write(password)
    
    return f'ZIP 파일을 성공적으로 해제하였습니다! 패스워드 : {password}'

def main():
    file = 'emergency_storage_key.zip'
    password_length = 6
    password_list = 'abcdefghijklmnopqrstuvwxyz1234567890'
    password_file = 'password.txt' # 2-1-(4) 암호를 푸는데 성공하면 암호는 password.txt로 저장
    try:
        result = unlock_zip(file,password_length,password_list,password_file)
        print(result)
    except zipfile.BadZipFile:
        print("올바르지 않은 ZIP 파일 형식.")
    except RuntimeError as e:
        print("ZIP 파일 암호 해제 중 오류 발생:", e)

if __name__ == "__main__":
    main()