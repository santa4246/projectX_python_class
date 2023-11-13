import os
import wave
import datetime
import pyaudio

class JarvisRecorder:
    def __init__(self):
        self.chunk = 1024  # 음성 데이터의 크기
        self.format = pyaudio.paInt16  # 음성 데이터의 포맷
        self.channels = 1  # 1: 모노, 2: 스테레오
        self.rate = 44100  # 샘플링 레이트
        self.record_folder = 'records'

        # records 폴더가 없으면 생성
        if not os.path.exists(self.record_folder):
            os.makedirs(self.record_folder)

        self.audio = pyaudio.PyAudio()

    def record_audio(self):
        stream = self.audio.open(format=self.format,
                                    channels=self.channels,
                                    rate=self.rate,
                                    input=True,
                                    frames_per_buffer=self.chunk)

        print('녹음을 시작합니다. 녹음을 종료하려면 Ctrl+C를 누르세요.')

        frames = []

        try:
            while True:
                data = stream.read(self.chunk)
                frames.append(data)
        except KeyboardInterrupt:
            print('녹음을 종료합니다.')

        stream.stop_stream()
        stream.close()

        self.save_audio(frames)

    def save_audio(self, frames):
        now = datetime.datetime.now()
        filename = f'{now.strftime("%Y%m%d-%H%M%S")}.wav'
        file_path = os.path.join(self.record_folder, filename)

        wf = wave.open(file_path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()

        print(f'녹음 파일이 저장되었습니다: {file_path}')

def main():
    try:
        recorder = JarvisRecorder()
        recorder.record_audio()
        
    except Exception as err :
        print('error: {0}'.format(err))

if __name__ == '__main__':
    main()