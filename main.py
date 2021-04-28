import os
from pyfiglet import Figlet

def art(text):
    cool_text = Figlet(font = "slant")
    os.system("cls")
    os.system('mode con: cols=75 lines=30')
    return str(cool_text.renderText(text))

if __name__ == "__main__":
    print(art("KAYN HVH"))