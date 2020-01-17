import pygame
from os import path
from settings import *
from sprites import *
import random
img_dir = path.join(path.dirname(__file__), 'img')



#iniciar pygames
pygame.init()

b_c =  pygame.transform.scale(Backgroundim, (1024, 576))
b_r = b_c.get_rect()
screen = pygame.display.set_mode((largo, alto))
dimscreen =  pygame.Surface(screen.get_size()).convert_alpha()
dimscreen.fill((0, 0, 0, 180))
pygame.display.set_caption("Tank")
clock = pygame.time.Clock()
font_name = pygame.font.match_font("arial")
taux = 0
hits = 0
disp = 0
time = 1

def draw_text(surf, text1, size, x, y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text1, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def menu1():
    Modo = 0
    modo2 = 0
    mapa = 0
    screen.fill(Background)
    draw_text(screen, "Tank", 64, largo / 2, alto / 8)
    draw_text(screen, "J1 W A S D para mover y LShift para disparar", 22, largo / 2, alto / 2)
    draw_text(screen, "J2 flechas para mover y RCtrl para disparar", 22, largo / 2, (alto /10)*6)
    draw_text(screen, "Presione cualquier para empezar", 22, largo / 2, (alto / 10)*8)
    pygame.display.flip()
    espera = True
    while espera:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                espera = False

    screen.fill(Background)
    draw_text(screen, "Presione 1 para un modo jugador", 22, largo / 2, alto / 2)
    draw_text(screen, "Presione 2 para modo 2 jugadores", 22, largo / 2, (alto / 10) * 6)
    draw_text(screen, "Presione ESC prara volver al menu principal", 22, largo / 2, (alto / 10) * 9)
    pygame.display.update()

    espera2 = True
    mn = True
    while espera2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                menu1()
            elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                Modo = 1
                espera2 = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                Modo = 2
                espera2 = False


    screen.fill(Background)
    draw_text(screen, "Presione 1 para mapa 1", 22, largo / 2, alto * 4 / 10)
    draw_text(screen, "Presione 2 para mapa 2", 22, largo / 2, (alto / 10) * 5)
    draw_text(screen, "Presione 3 para mapa 3", 22, largo / 2, (alto / 10) * 6)
    draw_text(screen, "Presione ESC prara volver al menu principal", 22, largo / 2, (alto / 10) * 9)
    pygame.display.flip()

    espera3 = True
    while espera3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP and  event.key == pygame.K_1:
                #if event.type == pygame.UP:
                mapa = 1
                espera3 = False
            elif event.type == pygame.KEYUP and  event.key == pygame.K_2:
                mapa = 2
                espera3 = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_3:
                    mapa = 3
                    espera3 = False
            elif event.type == pygame.KEYUP and  event.key == pygame.K_ESCAPE:
                menu1()
    if Modo == 2:
        screen.fill(Background)
        draw_text(screen, "Presione 1 para modo clasico", 22, largo / 2, alto / 2)
        draw_text(screen, "Presione 2 para para modo extra", 22, largo / 2, (alto / 10) * 6)
        draw_text(screen, "Presione ESC prara volver al menu principal", 22, largo / 2, (alto / 10) * 9)
        pygame.display.flip()
        espera4 = True
        while espera4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                    modo2 = 1
                    espera4 = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                    modo2 = 2
                    espera4 = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                    menu1()
    return Modo, mapa, modo2

def draw_grid():
    for x in range(0, largo, tile):
        pygame.draw.line(screen, WHITE, (x, 0), (x, alto))
    for y in range(0, alto, tile):
        pygame.draw.line(screen, WHITE, (0, y), (largo, y))

def load_data(m, n):
    game_folder = path.dirname(__file__)

    map_data = []
    global player1
    global player2

    if n == 1:
        mapa = 'mapa1.txt'
    elif n == 2:
        mapa = 'mapa2.txt'
    elif n == 3:
        mapa = 'mapa3.txt'
    try:
        with open(path.join(game_folder, mapa), 'rt') as f:
            for line in f:
                map_data.append(line)
        for row, tiles in enumerate(map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    wal = Wall(col, row)
                    wall.add(wal)
                    all_sprites.add(wal)
                if tile == 'P':
                    player1 = Player(col, row, playerimg1, 1)
                    players.add(player1)
                    all_sprites.add(player1)
                if m > 1:
                    if tile == "Q":
                        player2 = Player(col, row, playerimg2, 2)
                        players.add(player2)
                        all_sprites.add(player2)
                if m == 1:
                    if tile == "T":
                        targ = target(col, row)
                        targets.add(targ)
                        all_sprites.add(targ)

    except IOError as e:
        print("se ha encontrado un error con el archivo de records\n")
        print(e)

#correr juego
game_over = True
running = True
aux = True
no_item = True
while running:
    #velocidad de loops
    clock.tick(FPS)

    screen.fill(Background)
    screen.blit(b_c, b_r)
    if game_over:
        hits = 0
        time = 1
        disp = 0
        m1, mapa1, mult = menu1()
        load_data(m1, mapa1)
        game_over = False

    # Eventos de inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:
                shootsnd.play()
                player2.shoot()
            if event.key == pygame.K_LSHIFT:
                disp += 1
                shootsnd.play()
                player1.shoot()
        if event.key == pygame.K_ESCAPE and event.type == pygame.KEYUP:
            print("pausa")
            pausa = True

            screen.blit(dimscreen, (0, 0))
            draw_text(screen, "PAUSA", 50, largo / 2, alto / 2)
            draw_text(screen, "Espacio para reanudar", 15, largo / 2, alto / 2 * 6 / 10)
            draw_text(screen, "Esc para menu principal", 15, largo / 2, alto / 2 * 7 / 10)
            pygame.display.flip()
            while pausa:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                        pausa = False

                    if event.key == pygame.K_ESCAPE and event.type == pygame.KEYUP:
                        pausa = False
                        game_over = True
                        player1.kill()
                        if m1 == 2:
                            player2.kill()
                            for b in bullets2:
                                b.kill()
                        for b in bullets1:
                            b.kill()
                        for s in all_sprites:
                            s.kill()

                #    elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                 #        modo2 = 2
                 #        espera4 = False
                 #    elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                 #        menu1()
                 # for event in pygame.event.get():
                 #
    # Update
    all_sprites.update()

    if m1 == 1:
        #un jugador
        hits1 = pygame.sprite.groupcollide(targets, bullets1, True, True)   #se ve la colicion entre elementos de dos listas,
                                                                            #si hay colicion entre elementos, se eliminan
        for hit in hits1:
            hits +=1
        taux +=1

        if hits == 10:
            aux2 = True
            screen.fill(Background)
            seg = int(taux / 30)
            res = int(taux % 30)
            text = "Su tiempo es: " + str(seg) + "." + str(res)
            draw_text(screen, text, 22, largo / 2, alto * 3 / 10)
            text2 = "Disparos: " + str(disp)
            draw_text(screen, text2, 22, largo / 2, alto * 4 / 10)
            text3 = "Tiempo final " + str(seg + disp) + "." + str(res)
            draw_text(screen, text3, 22, largo / 2, alto * 5 / 10)
            pygame.display.flip()
            cont = 0
            while aux2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYUP:
                        player1.kill()
                        game_over = True
                        game_over = True
                        aux2 = False
    else:
        #dos jugadores
        if mult == 2:
            if no_item:
                Nitem = random.randrange(1, 4)
                coordx = random.randrange(0,gridalto)
                coordy = random.randrange(0, gridlargo)
                if Nitem == 1:
                    escu = defup(coordx, coordy)
                    sh.add(escu)
                    all_sprites.add(escu)
                    powerUp.add(escu)
                elif Nitem == 2:
                    bal = velBup(coordx, coordy)
                    ba.add(bal)
                    all_sprites.add(bal)
                    powerUp.add(bal)
                else:
                    mvel = velup(coordx, coordy)
                    sv.add(mvel)
                    all_sprites.add(mvel)
                    powerUp.add(mvel)
                no_item = False

            hitup = pygame.sprite.groupcollide(wall, powerUp, False, True)
            if hitup:
                no_item = True

            hitdefup1 = pygame.sprite.groupcollide(sh, bullets1, True, True)
            if hitdefup1:
                player1.escudo += 1
                no_item = True

            hitdefup2 = pygame.sprite.groupcollide(sh, bullets2, True, True)
            if hitdefup2:
                player2.escudo += 1
                no_item = True

            hitvelup1 = pygame.sprite.groupcollide(sv, bullets1, True, True)
            if hitvelup1:
                player1.vel += 5
                no_item = True

            hitvelup2 = pygame.sprite.groupcollide(sv, bullets2, True, True)
            if hitvelup2:
                player2.vel += 5
                no_item = True

            hitvelBup1 = pygame.sprite.groupcollide(ba, bullets1, True, True)
            if hitvelBup1:
                player1.vel_bala += 10
                no_item = True

            hitvelBup2 = pygame.sprite.groupcollide(ba, bullets2, True, True)
            if hitvelBup2:
                player2.vel_bala += 10
                no_item = True

        hits1 = pygame.sprite.spritecollide(player1, bullets2, True)
        if hits1:
            player1.escudo -= 1
            if player1.escudo <= 0:
                explosionsnd.play()
                player1.escudo = 1
                player2.score += 1
                player1.res()
                player2.res()
                if player2.score == 10:
                    screen.fill(Background)
                    draw_text(screen, "Gano J2", 22, largo / 2, alto * 2 / 5)
                    draw_text(screen, "Presione ESC para volver al menu principal", 22, largo / 2, alto * 5 / 6)
                    pygame.display.flip()
                    aux2 = True
                    player1.kill()
                    player2.kill()
                    for b in bullets1:
                        b.kill()
                    for b in bullets2:
                        b.kill()
                    while aux2:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                                game_over = True
                                aux2 = False

        hits2 = pygame.sprite.spritecollide(player2, bullets1, True)
        if hits2:
            player2.escudo -= 1
            if player2.escudo <= 0:
                explosionsnd.play()
                player2.escudo = 1
                player1.score += 1
                player1.res()
                player2.res()
                if player1.score == 10:
                    screen.fill(Background)
                    draw_text(screen, "Gano J1", 22, largo / 2, alto * 2 / 5)
                    draw_text(screen, "Presione ESC para volver al menu principal", 22, largo / 2, alto * 5 / 6)
                    pygame.display.flip()
                    player1.kill()
                    player2.kill()
                    for b in bullets1:
                        b.kill()
                    for b in bullets2:
                        b.kill()
                    aux2 = True
                    while aux2:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                                player1.kill()
                                game_over = True
                                aux2 = False
                                
        des = pygame.sprite.spritecollide(player2, bullets1, True)
        draw_text(screen, str(player1.score), 18, (largo/2 -10), 10)
        draw_text(screen, str(player2.score), 18, (largo / 2 + 10), 10)


    hitsb2 = pygame.sprite.groupcollide(wall, bullets2, False, True)
    hitsb = pygame.sprite.groupcollide(wall, bullets1, False, True)
    #draw_grid()
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()