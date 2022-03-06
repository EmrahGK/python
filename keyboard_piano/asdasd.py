import time
import pygame
pygame.init()

pygame.mixer.init()
win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Keyboard Piano")

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
do_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/51.wav"
do_diyez_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/52.wav"
re_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/53.wav"
re_diyez_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/54.wav"
mi_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/55.wav"
fa_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/56.wav"
fa_diyez_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/57.wav"
sol_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/58.wav"
sol_diyez_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/59.wav"
la_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/60.wav"
la_diyez_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/62.wav"
si_3 = "C:/Users/USER/Desktop/EMRAH/kodlar/Python/keyboard_piano/sounds/63.wav"

def cal(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.event.wait()



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pressed = pygame.key.get_pressed()


    if(pressed[pygame.K_q]):
        cal(fa_1)
    elif(pressed[pygame.K_w]):
        cal(sol_1)
    elif(pressed[pygame.K_e]):
        cal(la_1)
    elif(pressed[pygame.K_r]):
        cal(si_1)
    elif(pressed[pygame.K_t]):
        cal(do_2)
    elif(pressed[pygame.K_y]):
        cal(re_2)
    elif(pressed[pygame.K_u]):
        cal(mi_2)
    elif (pressed[pygame.K_i]):
        cal(fa_2)
    elif(pressed[pygame.K_o]):
        cal(sol_2)
    elif (pressed[pygame.K_p]):
        cal(la_2)
    elif (pressed[pygame.K_LEFTBRACKET]):
        cal(si_2)

    elif(pressed[pygame.K_ESCAPE]):
        pygame.quit()


