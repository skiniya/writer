import glob, os

from converter.full import fullAudio


def udalFile():
    os.chdir("./")
    for file in glob.glob("*.mp3"):
        os.remove(file)
        print(f"{file} удален")
    for file in glob.glob("*.wav"):
        os.remove(file)
        print(f"{file} удален")
    for file in glob.glob("*.txt"):
        os.remove(file)
        print(f"{file} удален")
        print("**********\nФайлов нет.")

if __name__ == '__main__':
    fullAudio()
else: udalFile()