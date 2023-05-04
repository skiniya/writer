# from google.colab import files
from faster_whisper import WhisperModel
from tqdm import tqdm
from pydub import AudioSegment
import glob, os

print("Начинаю работу с аудио:")
os.chdir("/content/")
for file in glob.glob("*.mp3"):
    print(file)
dst = "audio.wav"
sound = AudioSegment.from_mp3(file)
sound.set_channels(1)
sound = sound.set_frame_rate(16000)
sound = sound.set_channels(1)
sound.export(dst, format="wav")

# файл конвертируется в wav
def convert(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)


model = WhisperModel("large-v2", device="cuda", compute_type="int8_float16")

segments, info = model.transcribe("audio.wav", beam_size=1)
print("Длительность аудио: %s (%dс) " % (convert(info.duration), info.duration))
print('Расшифровка аудио в текст...')

myfile = open("text.txt", "a")
for segment in tqdm(segments, unit_scale=100, unit=' циклов', ascii=False, ncols=80, position=0,
                    total=(int(info.duration / 4)), dynamic_ncols=80, colour='#9ACD32'):
    myfile.write(segment.text)
myfile.close()

with open("text.txt", 'r+') as myfile:
    txt = myfile.read().replace('ё', 'е')
    myfile.seek(0)
    myfile.truncate()
    myfile.write(txt)
myfile.close()
print("\n📌 Готово! Можно забирать текст из txt файла.")