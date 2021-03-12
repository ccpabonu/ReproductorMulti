import pygame
a="imagen.jpg"
def reproducirImagenes(a):
    imgs = []
    imgs.append(pygame.image.load(a))

    pygame.init()

    dimensiones = [1000, 650]
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Audio y imagenes")

    listaRects = [
        [imgs[0],[0, 0], [1000, 650]]
    ]

    game_over = False
    reloj = pygame.time.Clock()

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.MOUSEBUTTONDOWN :
                pos = pygame.mouse.get_pos()

        for cuadro in listaRects:
            picture = pygame.transform.scale(cuadro[0], cuadro[2])
            pantalla.blit(picture, cuadro[1])
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()

#reproducirImagenes(a)
#-----------------------------------------------------------------------------------------------------------------------------

def reproducirMusica(b):

    pygame.init()

    pantalla = pygame.display.set_mode((470, 300), 0, 32)
    pygame.display.set_caption("Modulo Music")

    reloj = pygame.time.Clock()

    pygame.mixer.music.load(b)
    pygame.mixer.music.play(1)
    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_p:
                    pygame.mixer.music.stop()
        reloj.tick(20)
        pygame.display.update()

#reproducirMusica("musica.mp3")


