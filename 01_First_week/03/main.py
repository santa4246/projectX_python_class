import csv
import json
from datetime import datetime

# 로그 파일을 읽어 리스트로 변환
with open('mission_computer_main.log', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    logs_list = []
    for row in reader:
        timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        event = row[1]
        message = row[2]
        logs_list.append({'timestamp': timestamp, 'event': event, 'message': message})

# 리스트를 화면에 출력
print("로그 리스트:")
print(logs_list)

# 리스트를 시간의 역순으로 정렬
logs_list.sort(key=lambda x: x['timestamp'], reverse=True)

# 정렬된 리스트를 화면에 출력
print("시간의 역순으로 정렬된 로그 리스트:")
print(logs_list)

# 리스트를 사전 객체로 변환
logs_dict = {'logs': logs_list}

# 사전 객체를 JSON 파일로 저장
with open('mission_computer_main.json', 'w') as json_file:
    json.dump(logs_dict, json_file)

print("mission_computer_main.json 파일이 생성되었습니다.")
