import torch
from pathlib import Path
from pydub import AudioSegment
def cutAudio():
    import fnmatch
    import os

    print("Начинаю работу с аудио:")

    os.chdir("./")
    for file in glob.glob("*.mp3"):
        print(file)

    def time_to_sec(t1):
        h, m, s = map(int, t1.split(':'))
        return h * 3600 + m * 60 + s
        print("Введите начальное время в формате hh:mm:ss")
        t1 = input()
        t11: int = time_to_sec(t1)
    def time_to_sec(t2):
        h, m, s = map(int, t2.split(':'))
        return h * 3600 + m * 60 + s
        print("Введите конечное время в формате hh:mm:ss")
        t2 = input()
        t22: int = time_to_sec(t2)

        print("Запускаю процесс...")

        t_start = t11 * 1000  # если нужно от начала - 0 * 1000
        t_end = t22 * 1000  # 60 секунд - до 1-й минуты
        new_audio = AudioSegment.from_mp3(file)
        a = new_audio[t_start:t_end]
        a.export("fragment.mp3", format="mp3")

        print("📌 Готово! Аудио вырезано, называется fragment.mp3.")
    else:
        print("\nРабота завершена.")


if __name__ == '__main__':
    cutAudio()