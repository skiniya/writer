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

#print("Сначала загружаем сюда наше аудио (для ЧАСТИЧНОГО написания), которое переименовано в цифры\n🔻🔻🔻🔻🔻\n")
#from google.colab import files
#uploaded = files.upload()
for file in os.listdir('/content/'):
    if fnmatch.fnmatch(file, '*.mp3'):
        dir : str = file
        id_audio = dir[:-4] 
def time_to_sec(t1):
    h, m, s = map(int, t1.split(':'))
    return h * 3600 + m * 60 + s
print("*****************\nВведите начальное время в формате hh:mm:ss")
t1 = input()
t11 : int = time_to_sec(t1)
def time_to_sec(t2):
    h, m, s = map(int, t2.split(':'))
    return h * 3600 + m * 60 + s
print("*****************\nВведите конечное время в формате hh:mm:ss")
t2 = input()
t22 : int = time_to_sec(t2)
from pydub import AudioSegment
t_start = t11 * 1000  #      если нужно от начала - 0 * 1000
t_end = t22 * 1000 #      60 секунд - до 1-й минуты
newAudio = AudioSegment.from_mp3(f"{id_audio}.mp3")
a = newAudio[t_start:t_end]
a.export("fragment.mp3", format="mp3")

	model_size = "medium" #лучшее воспроизведение текста
	model = WhisperModel(model_size, device="cpu", compute_type="int8")
	segments, info = model.transcribe("fragment.mp3", beam_size=50)
	print("*****************\nДлина аудио: %s (%dс) " % (convert(info.duration), info.duration))
	print('*****************\nТекст аудио:')
	myfile = open(f"{id_audio}+fragment.txt", "a")

	for segment in segments:
    		myfile.write(segment.text)
    		print("[%s - %s] %s" % (convert(segment.start), convert(segment.end), segment.text)) 
	myfile.close()

	with open(f"{id_audio}+fragment.txt", 'r+') as myfile:
    		txt = myfile.read().replace('ё', 'е')
    		myfile.seek(0)
    		myfile.truncate()
    		myfile.write(txt)
	myfile.close()

	with open(f"{id_audio}+fragment.txt") as myfile:
   		tm = myfile.read() 
		with open(f"{id_audio}+fragment.txt", 'w') as f:
    		print(t1,  tm, sep='\n', file=f)
    		f.seek(0, os.SEEK_END)
    		f.write(t2)
print("*****************\nГотово!\n✔️✔️✔️✔️✔️")