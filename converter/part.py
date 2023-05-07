# from google.colab import files
import fnmatch
import os

print("Начинаю работу с аудио:")

for file in os.listdir('/content/'):
    if fnmatch.fnmatch(file, '*.mp3'):
        dir : str = file
        id_audio = dir[:-4]
print(id_audio+".mp3")

def time_to_sec(t1):
    h, m, s = map(int, t1.split(':'))
    return h * 3600 + m * 60 + s
print("Введите начальное время в формате hh:mm:ss")
t1 = input()
t11 : int = time_to_sec(t1)
def time_to_sec(t2):
    h, m, s = map(int, t2.split(':'))
    return h * 3600 + m * 60 + s
print("Введите конечное время в формате hh:mm:ss")
t2 = input()
t22 : int = time_to_sec(t2)

print("Запускаю процесс...")

from pydub import AudioSegment
t_start = t11 * 1000  #      если нужно от начала - 0 * 1000
t_end = t22 * 1000 #      60 секунд - до 1-й минуты
newAudio = AudioSegment.from_mp3(id_audio+".mp3")
a = newAudio[t_start:t_end]
a.export("fragment.mp3", format="mp3")

print("📌 Готово! Аудио вырезано, называется fragment.mp3."