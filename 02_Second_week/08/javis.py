import os
import wave
import datetime
import pyaudio
import speech_recognition as sr
import csv

class JarvisRecorder:
    def __init__(self):
        self.chunk = 1024  # 음성 데이터의 크기
        self.format = pyaudio.paInt16  # 음성 데이터의 포맷
        self.channels = 1  # 1: 모노, 2: 스테레오
        self.rate = 44100  # 샘플링 레이트
        self.record_folder = 'records'
        self.csv_folder = 'csv'

        # records 폴더가 없으면 생성
        if not os.path.exists(self.record_folder):
            os.makedirs(self.record_folder)

        # csv 폴더가 없으면 생성
        if not os.path.exists(self.csv_folder):
            os.makedirs(self.csv_folder)

        self.audio = pyaudio.PyAudio()
        self.recognizer = sr.Recognizer()

    def convert_to_text(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio_data = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio_data, language='ko-KR')
                print("음성을 텍스트로 변환했습니다:", text)
                self.save_to_csv(audio_file, text)
            except sr.UnknownValueError:
                print("음성을 인식할 수 없습니다.")
            except sr.RequestError as e:
                print(f"Google API에 요청할 수 없습니다. 에러: {e}")

    def save_to_csv(self, audio_file, text):
        filename = os.path.splitext(os.path.basename(audio_file))[0] + ".csv"
        file_path = os.path.join(self.csv_folder, filename)

        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['시간', '인식된 텍스트'])
            csv_writer.writerow([datetime.datetime.now().strftime('%H:%M:%S'), text])

        print(f"CSV 파일이 저장되었습니다: {file_path}")


def main():
    try:
        recorder = JarvisRecorder()
        recorder.convert_to_text('records')
        
    except Exception as err :
        print('error: {0}'.format(err))

if __name__ == '__main__':
    main()