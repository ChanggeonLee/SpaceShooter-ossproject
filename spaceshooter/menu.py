import pygame
from os import path
def main_menu():
    global screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "main.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
                pygame.quit()
                quit() 
        else:
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH/2, HEIGHT/2)
            draw_text(screen, "or [Q] To Quit", 30, WIDTH/2, (HEIGHT/2)+40)
            pygame.display.update()

    #pygame.mixer.music.stop()
    ready = pygame.mixer.Sound(path.join(sound_folder,'getready.ogg'))
    ready.play()
    screen.fill(BLACK)
    draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/2)
    pygame.display.update()
