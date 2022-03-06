import pygame
from time import sleep
from pynput.keyboard import Key, Listener
#33 fa
pygame.init()
pygame.mixer.init()
print("""
DUMBASS KEYBOARD PIANO

_____2______3______4___________6_____7__________9______0_____?______
|   |██|   |██|   |██|   |    |██|  |██|   |   |██|   |██|  |██|   |  
|   |██|   |██|   |██|   |    |██|  |██|   |   |██|   |██|  |██|   |
|   |██|   |██|   |██|   |    |██|  |██|   |   |██|   |██|  |██|   |
|   |██|   |██|   |██|   |    |██|  |██|   |   |██|   |██|  |██|   |
|   |██|   |██|   |██|   |    |██|  |██|   |   |██|   |██|  |██|   |
|     |     |      |     |     |     |     |     |     |     |     |
|  Q  |  W  |  E   |  R  |  T  |  Y  |  U  |  I  |  O  |  P  |  Ğ  |
|_____|_____|______|_____|_____|_____|_____|_____|_____|_____|_____|
""")


fa_1 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/33.wav"
fa_diyez_1 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/34.wav"
sol_1 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/35.wav"
sol_diyez_1 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/36.wav"
la_1 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/37.wav"
la_diyez_1 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/38.wav"
si_1 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/39.wav"
do_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/40.wav"
do_diyez_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/41.wav"
re_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/42.wav"
re_diyez_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/43.wav"
mi_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/44.wav"
fa_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/45.wav"
fa_diyez_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/46.wav"
sol_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/47.wav"
sol_diyez_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/48.wav"
la_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/49.wav"
la_diyez_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/50.wav"
si_2 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/51.wav"


class Note():
    def __init__(self, file):
        self.file = file

    def cal(self,file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()


q = Note(fa_1)
w = Note(sol_1)
e = Note(la_1)
r = Note(si_1)
t = Note(do_2)

pygame.mixer.Sound(fa_1)

def on_press(key):
    print(f'Press On: {key}')
    return key

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()


# def play():
#     while True:
#         play()
#         sleep(0.8)