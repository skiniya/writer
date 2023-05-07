import glob, os
from converter import udal

os.chdir("/content/")
for file in glob.glob("*.mp3"):
    os.remove(file)
    print(f"{file} удален")
for file in glob.glob("*.wav"):
    os.remove(file)
    print(f"{file} удален")
for file in glob.glob("*.txt"):
    os.remove(file)
    print(f"{file} удален")    
print("**********\nНичего нет.")