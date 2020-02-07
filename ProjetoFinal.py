import pygame
import pygame.freetype
import random
import sys
from pygame.locals import *

def main():
    pygame.init()    
    TELATAM = (1280, 800)
    DISPLAY = pygame.display.set_mode(TELATAM)
    PONTOS = 0
    FONT = pygame.freetype.Font("NotoSans-Regular.ttf", 28)
   
    while True:
        mouse = pygame.mouse.get_pos()
        #for para verificar a operação relizada pelo mouse e caso seja fechar janela, desliga o programa
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
        ##
        #cor de background
        DISPLAY.fill((226, 49, 35))
        ##
        #desenhar os botoes de niveis consuante o display, coordenada a coordenada
        y = 250
        for n in range(6):
            pygame.draw.rect(DISPLAY, (0,0,0), (550, y, 120, 35), 4)
            y = y + 50
            FONT.render_to(DISPLAY, (590, 255), "3x4", (0, 0, 0))
            FONT.render_to(DISPLAY, (590, 305), "4x4", (0, 0, 0))
            FONT.render_to(DISPLAY, (590, 355), "5x4", (0, 0, 0))
            FONT.render_to(DISPLAY, (590, 405), "6x4", (0, 0, 0))
            FONT.render_to(DISPLAY, (590, 455), "6x5", (0, 0, 0))
            FONT.render_to(DISPLAY, (590, 505), "6x6", (0, 0, 0))
        
        if(670 > mouse[0] > 550 and 285 > mouse[1] > 250):
            pygame.draw.rect(DISPLAY, (255,255,255), (550, 250, 120, 35), 4)
            FONT.render_to(DISPLAY, (590, 255), "3x4", (255, 255, 255))
            if(event.type == pygame.MOUSEBUTTONUP):
                GAMEDISPLAY(DISPLAY, 12, 6, 500, 200, 4, 3)
        if(670 > mouse[0] > 550 and 335 > mouse[1] > 300):
            pygame.draw.rect(DISPLAY, (255,255,255), (550, 300, 120, 35), 4)
            FONT.render_to(DISPLAY, (590, 305), "4x4", (255, 255, 255))
            if(event.type == pygame.MOUSEBUTTONUP):
                GAMEDISPLAY(DISPLAY, 16, 8, 500, 150, 4, 3)
        if(670 > mouse[0] > 550 and 385 > mouse[1] > 350):
            pygame.draw.rect(DISPLAY, (255,255,255), (550, 350, 120, 35), 4)
            FONT.render_to(DISPLAY, (590, 355), "5x4", (255, 255, 255))
            if(event.type == pygame.MOUSEBUTTONUP):
                GAMEDISPLAY(DISPLAY, 20, 10, 500, 150, 4, 3)
        if(670 > mouse[0] > 550 and 435 > mouse[1] > 400):
            pygame.draw.rect(DISPLAY, (255,255,255), (550, 400, 120, 35), 4)
            FONT.render_to(DISPLAY, (590, 405), "6x4", (255, 255, 255))
            if(event.type == pygame.MOUSEBUTTONUP):
                GAMEDISPLAY(DISPLAY, 24, 12, 500, 100, 4, 3)
        if(670 > mouse[0] > 550 and 485 > mouse[1] > 450):
            pygame.draw.rect(DISPLAY, (255,255,255), (550, 450, 120, 35), 4)
            FONT.render_to(DISPLAY, (590, 455), "6x5", (255, 255, 255))
            if(event.type == pygame.MOUSEBUTTONUP):
                GAMEDISPLAY(DISPLAY, 30, 15, 450, 100, 5, 4)
        if(670 > mouse[0] > 550 and 535 > mouse[1] > 500):
            pygame.draw.rect(DISPLAY, (255,255,255), (550, 500, 120, 35), 4)
            FONT.render_to(DISPLAY, (590, 505), "6x6", (255, 255, 255))
            if(event.type == pygame.MOUSEBUTTONUP):
                GAMEDISPLAY(DISPLAY, 36, 18, 400, 100, 6, 5)
        ###
        #Botao de exit, caso o utilizador passe o mouse por cima do botão este muda de cor, e se clicar nele irá sair do jogo
        FONT.render_to(DISPLAY, (105, 715), "EXIT", (238, 177, 22))
        pygame.draw.rect(DISPLAY, (238, 177, 22), (50, 700, 160, 50), 4)
        if(210 > mouse[0] > 50 and 750 > mouse[1] > 700):
            pygame.draw.rect(DISPLAY, (255,255,255), (50, 700, 160, 50), 4)
            FONT.render_to(DISPLAY, (105, 715), "EXIT", (255, 255, 255))
            if(event.type == pygame.MOUSEBUTTONUP):
                pygame.quit()
                sys.exit()
        ###
        pygame.display.flip()


def GAMEDISPLAY(DISPLAY, NCARTAS, NCORES, x, y, Nlinhas, a):
    
    TELATAM = (1280, 800)
    DISPLAY = pygame.display.set_mode(TELATAM)
    PONTOS = 0
    FONT = pygame.freetype.Font("NotoSans-Regular.ttf", 20)
    FONT2 = pygame.freetype.Font("NotoSans-Regular.ttf", 36)
    FONT3 = pygame.freetype.Font("NotoSans-Regular.ttf", 28)
    DISPLAY.fill((10, 106, 78))
    FONT.render_to(DISPLAY, (30, 30), "PONTOS: " , (0, 0, 0))

    #variáveis utlizadas para a posição das cartas
    b = a
    normalizador = x
    coordx = x  
    coordy = y
    #CORES        R    G   B
    ROSA_SECO = (204, 47, 72)
    VERMELHO_ESCURO = (123, 14, 14)
    AZUL_BEBE = (175, 231, 229)
    ROSA_VELHO = (198, 71, 116)
    ROXO = (34, 20, 39)
    CINZENTO = (217, 211, 202)
    CASTANHO_CLARO = (209, 139, 74)
    AZUL_ESCURO = (19, 51, 94)
    VERDE_FLURESCENTE = (6, 228, 5)
    AMARELO_TORRADO = (213, 133, 10)
    CASTANHO_AVERMELHADO = (144, 33, 4)
    LARANJA = (255, 70, 0)
    AMARELO = (255, 255, 0)
    VERDE_AZULADO = (0, 255, 150)
    PURPURA = (135, 95, 255)
    CASTANHO_ESGOTO = (150, 95, 0)
    VERMELHO_LAGOSTA = (255, 100, 100)
    LARANJA_CLARO = (255, 140, 0)
    ###
    #BARALHAR AS CARTAS
    CORES = [ROSA_SECO,VERDE_FLURESCENTE, VERMELHO_ESCURO, AZUL_BEBE, ROSA_VELHO, ROXO, CINZENTO, CASTANHO_CLARO, AZUL_ESCURO, AMARELO_TORRADO, CASTANHO_AVERMELHADO, LARANJA, VERDE_AZULADO, AMARELO, PURPURA, CASTANHO_ESGOTO, VERMELHO_LAGOSTA, LARANJA_CLARO]
    POSICAO = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]
    CORES_SELECIONADAS = []
    ORDENADO = []
    for i in range(NCORES):
        CORES_SELECIONADAS.append(CORES[i])
    for i in range(NCARTAS):
        ORDENADO.append(POSICAO[i])
    random.shuffle(ORDENADO)
    ###
    #listas utilizadas para guardas as posições e as cores das cartas
    POSREC = []
    CARDCOR = []
    CORSREVEL = []
    POSREVEL = []
    INDEX = []
    REVEL = 0
    OUT = 0 
    CLICK = 1
    ###
    #guarda as cores e as coordenadas de forma ordenada para o index nas duas listas se referir á mesma carta
    for i in range(NCARTAS):
        POSREC.append(pygame.Rect(x, y, 50, 70))
        CARDCOR.append(CORES_SELECIONADAS[ORDENADO[i]])   
        x = x + 60
        if(i == a):
            y = y + 80
            x = normalizador
            a += Nlinhas
    ###
    #desenha as cartas escondidas, o numero altera conforme o modo de jogo
    for i in range(NCARTAS):
        pygame.draw.rect(DISPLAY,(0,0,0), (coordx, coordy, 50, 70), 0)
        coordx += 60
        if(i == b):
            coordy += 80
            coordx = normalizador
            b += Nlinhas
    ###
    while(True):
        mouse = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        #desenhar novo display
        pygame.draw.rect(DISPLAY, (10, 106, 78), (120, 20, 100, 40), 0)
        if(PONTOS < 0):
            PONTOS = 0
        FONT.render_to(DISPLAY, (120, 30), str(PONTOS), (0, 0, 0))
        ###
        #inicio de jogo com um for que detecta qual o evento de pygame
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
            #caso o evento seja clicar nas cartas inicia-se um for que irá percorrer o numero de cartas
            if(event.type == pygame.MOUSEBUTTONUP):  
                for i in range(NCARTAS):
                    #se a posicao do mouse estiver dentro do rect irá revelar a carta, adicionando-a a uma lista para utilizacao posterior e adicionar a posicao do rect noutra lista
                    if(POSREC[i][0]+ 50 > mouse[0] > POSREC[i][0] and POSREC[i][1] + 70 > mouse[1] > POSREC[i][1]):
                        pygame.draw.rect(DISPLAY, CARDCOR[i], POSREC[i] , 0)
                        CORSREVEL.append(CARDCOR[i])
                        POSREVEL.append(POSREC[i])
                        INDEX.append(i)
                        REVEL += 1
                    #caso sejam reveladas 2 cartas irá camparar as cores de cada uma
                    if(REVEL == 2):
                        if(POSREVEL[0] != POSREVEL[1]):
                            pygame.display.flip()
                            comparado = COMPARE(CORSREVEL)
                            pygame.time.wait(800)
                            #se for verdade irá retira-las das listas usadas e adiciona pontos
                            if(comparado):
                                REVEL = 0
                                PONTOS += 100
                                OUT += 2
                                POSREC[INDEX[0]] = pygame.Rect(10, 10, 1, 1)
                                POSREC[INDEX[1]] = pygame.Rect(10, 10, 1, 1)
                                CORSREVEL.pop(1)
                                CORSREVEL.pop(0)
                                POSREVEL.pop(1)
                                POSREVEL.pop(0)
                                INDEX.pop(1)
                                INDEX.pop(0)
                                CLICK = 1
                            ###
                            #se for falso irá retira-las das listas usadas, retirar pontos e voltar a por o rect preto
                            else:
                                PONTOS -= 20 * CLICK
                                CLICK += 1
                                REVEL = 0
                                pygame.draw.rect(DISPLAY, (0, 0, 0), POSREVEL[0] , 0)
                                pygame.draw.rect(DISPLAY, (0, 0, 0), POSREVEL[1] , 0)
                                CORSREVEL.pop(1)
                                CORSREVEL.pop(0)
                                POSREVEL.pop(1)
                                POSREVEL.pop(0)
                                INDEX.pop(1)
                                INDEX.pop(0)
                            ###
                        #Para não ficar com mais de 2 cartas reveladas esta condicao retira a revelada a mais
                        else:
                            REVEL -= 1
                            CORSREVEL.pop(1)
                            POSREVEL.pop(1)
                            INDEX.pop(1)
                        ###
                    #quando ficar sem cartas no display o jogador ganha o nivel
                    if(OUT == NCARTAS):
                        DISPLAY.fill((10, 106, 78))
                        FONT2.render_to(DISPLAY, (500, 300), "Congratulations!" , (0, 0, 0))
                    ###
        #botao para voltar ao main
        FONT3.render_to(DISPLAY, (105, 715), "EXIT", (238, 177, 22))
        pygame.draw.rect(DISPLAY, (238, 177, 22), (50, 700, 160, 50), 4)
        if(210 > mouse[0] > 50 and 750 > mouse[1] > 700):
            pygame.draw.rect(DISPLAY, (255,255,255), (50, 700, 160, 50), 4)
            FONT3.render_to(DISPLAY, (105, 715), "EXIT", (255, 255, 255))
            if(event.type == pygame.MOUSEBUTTONUP):
                main()
        pygame.display.flip()
  
def COMPARE(COMPARED):
    #Compara as cores de cada carta
    if(COMPARED[0] == COMPARED[1]):
        return True
    else:
        return False

#Inicia o main
main()