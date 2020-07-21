import pygame


pygame.init()

window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("animeGame")

FPS = pygame.time.Clock()
FPS.tick(60)

x, y = 300, 100


k_d_pressed = False
k_a_pressed = False
k_w_pressed = False
k_s_pressed = False

imagen = pygame.image.load("anime.png")  
imagen = pygame.transform.scale(imagen, (100, 200))

out = False
while not out:
    event = pygame.event.poll()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            out=True
        elif event.key == pygame.K_d:
            k_d_pressed = True
        elif event.key == pygame.K_a:
            k_a_pressed = True
        elif event.key == pygame.K_s:
            k_s_pressed = True
        elif event.key == pygame.K_w:
            k_w_pressed = True
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            k_d_pressed = False
        elif event.key == pygame.K_a:
            k_a_pressed = False
        elif event.key == pygame.K_s:
            k_s_pressed = False
        elif event.key == pygame.K_w:
            k_w_pressed = False
   


    if k_d_pressed:
        x = x + 1
    if k_a_pressed:
        x = x - 1
    if k_s_pressed:
        y = y + 1
    if k_w_pressed:
        y = y - 1
    
    
    window.fill((0,0,0))
    window.blit(imagen, (x, y))
    pygame.display.flip()