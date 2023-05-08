# from google.colab import files
!pip install git+https://github.com/skiniya/writer.git --quiet --disable-pip-version-check
!pip install faster_whisper
!pip install pydub
!pip install tqdm

from faster_whisper import WhisperModel
from tqdm import tqdm
from pydub import AudioSegment
import fnmatch
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


    import torch

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    if torch.cuda.is_available():
        device = torch.device('cuda')
        model = WhisperModel("large-v2", device="cuda", compute_type="int8_float16")
        print("\nМодель расшифровки текста на GPU: large-v2.\n")
    else:
        device = torch.device('cpu')
        model = WhisperModel("medium", device="cpu", compute_type="int8")
        print("\nМодель расшифровки текста на CPU: medium.\n")

    # model = WhisperModel("large-v2", device="cuda", compute_type="int8_float16")
    # model = WhisperModel("large-v2", device="cpu", compute_type="int8")

    segments, info = model.transcribe("audio.wav", beam_size=1)
    print("Длительность аудио: %s (%dс) " % (convert(info.duration), info.duration))
    print('\nРасшифровка аудио в текст...')

    myfile = open("text.txt", "a")
    for segment in tqdm(segments, unit_scale=100, unit=' циклов', ascii=False, ncols=100, position=0,
                        total=(int(info.duration / 4)), dynamic_ncols=100, colour='#9ACD32'):
        myfile.write(segment.text)
        # print("[%s] %s" % (convert(segment.start), segment.text))
    myfile.close()

    with open("text.txt", 'r+') as myfile:
        txt = myfile.read().replace('ё', 'е')
        myfile.seek(0)
        myfile.truncate()
        myfile.write(txt)
        myfile.close()
    print("\n\n📌 Готово! Можно забирать текст из txt файла.")
else:
    print("\nРабота завершена.")

if __name__ == '__main__':
    print("Мэйн")

#    convert()


