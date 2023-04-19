# from google.colab import files
from faster_whisper import WhisperModel
import fnmatch
import os


def convert(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)


print("Начинаю...")
for file in os.listdir('/content/'):
    if fnmatch.fnmatch(file, '*.mp3'):
        dir: str = file
        id_audio = dir[:-4]

        model_size = "medium"  # лучшее воспроизведение текста
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        segments, info = model.transcribe(f"{id_audio}.mp3", beam_size=5)
        print("*****************\nДлина аудио: %s (%dс) " % (convert(info.duration), info.duration))
        print('*****************\nТекст аудио:')
        myfile = open(f"{id_audio}.txt", "a")

        for segment in segments:
            myfile.write(segment.text)
            print("[%s - %s] %s" % (convert(segment.start), convert(segment.end), segment.text))
        myfile.close()

        with open(f"{id_audio}.txt", 'r+') as myfile:
            txt = myfile.read().replace('ё', 'е')
            myfile.seek(0)
            myfile.truncate()
            myfile.write(txt)
        myfile.close()

        print("*****************\nГотово! Можно забрать текст из txt файла.\n✔️✔️✔️✔️✔️")
