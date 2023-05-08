from autocorrect import Speller
import glob, os
def autoCorrect():
    print("Начинаю работу с текстом:")

    os.chdir("./")
    for file in glob.glob("*.txt"):
        print(file)
        spell = Speller('ru')
        f = open("text.txt")
        a = f.read()
        result = spell(a)

        myfile = open("text_correct.txt", "a")
        myfile.write(result)
        myfile.close()

        Path('text_correct.txt').write_text(Path('text_correct.txt').read_text().replace('ё', 'е'))
        Path('text_correct.txt').write_text(Path('text_correct.txt').read_text().replace('Исус', 'Иисус'))
        Path('text_correct.txt').write_text(Path('text_correct.txt').read_text().replace('Узя', 'Уззия'))
        Path('text_correct.txt').write_text(Path('text_correct.txt').read_text().replace('Ося', 'Уззия'))
        Path('text_correct.txt').write_text(Path('text_correct.txt').read_text().replace('Узю', 'Уззию'))
        Path('text_correct.txt').write_text(Path('text_correct.txt').read_text().replace('Узия', 'Уззия'))

        print("\nГотово! Можно забирать текст из text_correct.txt.")
    else:
        print("\nРабота завершена.")


if __name__ == '__main__':
    autoCorrect()