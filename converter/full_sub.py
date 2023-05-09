import torch
from pathlib import Path
def convert(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)
def fullAudio_sub():
    from faster_whisper import WhisperModel
    from tqdm import tqdm
    from pydub import AudioSegment
    import fnmatch
    import glob, os

    print("Начинаю работу с аудио:")

    os.chdir("./")
    for file in glob.glob("*.mp3"):
        print(file)
        dst = "audio.wav"
        sound = AudioSegment.from_mp3(file)
        sound.set_channels(1)
        sound = sound.set_frame_rate(16000)
        sound = sound.set_channels(1)
        sound.export(dst, format="wav")

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        if torch.cuda.is_available():
            device = torch.device('cuda')
            model = WhisperModel("large-v2", device="cuda", compute_type="int8_float16")
            print("\nМодель расшифровки текста на GPU: large-v2.\n")
        else:
            device = torch.device('cpu')
            model = WhisperModel("medium", device="cpu", compute_type="int8")
            print("\nМодель расшифровки текста на CPU: medium.\n")

        segments, info = model.transcribe("audio.wav", beam_size=1)
        print("Длительность аудио: %s (%dс) " % (convert(info.duration), info.duration))
        print('\nРасшифровка аудио в текст...')

        myfile = open("text.txt", "a")
        for segment in segments:
            print("%s: %s" % (convert(segment.start), segment.text))
            myfile.write(segment.text)
        myfile.close()

        Path('text.txt').write_text(Path('text.txt').read_text().replace('ё', 'е'))
        Path('text.txt').write_text(Path('text.txt').read_text().replace('Исус', 'Иисус'))
        Path('text.txt').write_text(Path('text.txt').read_text().replace('Узя', 'Уззия'))
        Path('text.txt').write_text(Path('text.txt').read_text().replace('Ося', 'Уззия'))
        Path('text.txt').write_text(Path('text.txt').read_text().replace('Уся', 'Уззия'))
        Path('text.txt').write_text(Path('text.txt').read_text().replace('Узю', 'Уззию'))
        Path('text.txt').write_text(Path('text.txt').read_text().replace('Узия', 'Уззия'))
        Path('text.txt').write_text(Path('text.txt').read_text().replace('Уния', 'Уззия'))

        print("\nСлова в тексте заменены.")
        print("\n📌 Можно забирать текст из txt файла.")
    else:
        print("\nРабота завершена.")


if __name__ == '__main__':
    fullAudio_sub()