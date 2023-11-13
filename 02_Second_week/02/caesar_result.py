# password.txt 파일을 읽어오기
def read_password_file(file_path='password.txt'):
    with open(file_path, 'r') as file:
        password = file.read().strip()
    return password

# caesar_cipher_decode() 함수는 풀어야 하는 문자열을 파라메터로 추가하고 이때 파라메터의 이름은 target_text으로 
def caesar_cipher_decode(target_text, shift):
    result_text = ''
    for char in target_text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)  # 암호를 푸는 계산식
            result_text += decoded_char
        else:
            result_text += char # 알파벳이 아닌 문자는 그대로 추가
    return result_text

# 자리수에 따라서 해독된 결과를 출력
def decrypt_and_print_result(password, target_text):
    for shift in range(26):
        decoded_result = caesar_cipher_decode(target_text, shift)
        print(f"Shift: {shift}, Decoded Result: {decoded_result}")

# 파일에서 암호를 읽어옴
password_file_path = 'password.txt'
password = read_password_file(password_file_path)

# 풀어야 하는 문자열을 password.txt에서 읽어옴
with open(password_file_path, 'r') as target_file:
    target_text = target_file.read().strip()

# 자리수에 따라서 해독된 결과 출력
print("1차 해독 결과:")
decrypt_and_print_result(password, target_text)

# 추가 질문: 몇 번째 자리 수로 암호가 해독되었는지 입력
shift_input = input("몇 번째 자리수로 암호가 해독되었나요? (숫자 입력): ")

# 결과를 저장할 경로
result_file_path = 'result.txt'

try:
    shift = int(shift_input)
    if 0 <= shift < 26:
        decoded_result = caesar_cipher_decode(target_text, shift)
        with open(result_file_path, "w") as result_file:
            result_file.write(decoded_result)
        print(f"암호가 {shift}번째 자리수로 해독됩니다.")
        print(f"해독된 결과를 {result_file_path}에 저장했습니다.")
    else:
        print("올바른 범위의 자리 수를 입력하세요 (0~25).")
except ValueError:
    print("올바른 숫자를 입력하세요.")
