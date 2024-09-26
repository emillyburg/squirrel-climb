import pygame, sys
import math

pygame.init()

#definições iniciais

largura_janela = 400
altura_janela = 600
pygame.display.set_caption('    Squirrel Climb')
clock = pygame.time.Clock()
fgExit = False
personagemImg = pygame.image.load('esquilo.png')
DEFAULT_PERSONAGEMIMG_SIZE = (50, 50)
personagemImg=pygame.transform.scale(personagemImg,DEFAULT_PERSONAGEMIMG_SIZE)
#começo


nuvem1 = pygame.image.load('nuvem1.png')
nuvem1Img = pygame.transform.scale(nuvem1, (100, 100))
nuvem2 = pygame.image.load('nuvem2.png')
nuvem2Img = pygame.transform.scale(nuvem2, (100, 100))
nuvem3 = pygame.image.load('nuvem3.png')
nuvem3Img = pygame.transform.scale(nuvem3, (100, 100))
nuvem4 = pygame.image.load('nuvem4.png')
nuvem4Img = pygame.transform.scale(nuvem4, (100, 100))
nuvem5 = pygame.image.load('nuvem5.png')
nuvem5Img = pygame.transform.scale(nuvem5, (100, 100))
nuvem6 = pygame.image.load('nuvem6.png')
nuvem6Img = pygame.transform.scale(nuvem6,(100, 100))
nuvem7 = pygame.image.load('nuvem7.png')
nuvem7Img = pygame.transform.scale(nuvem7, (100, 100))
nuvem8 = pygame.image.load('nuvem8.png')
nuvem8Img = pygame.transform.scale(nuvem8, (100, 100))
nuvem9 = pygame.image.load('nuvem9.png')
nuvem9Img = pygame.transform.scale(nuvem9, (100, 100))
nuvem10 = pygame.image.load('nuvem10.png')
nuvem10Img = pygame.transform.scale(nuvem10, (100, 100))
#final nuvens 
personagem3 = pygame.image.load('noz.png')
personagem3Img = pygame.transform.scale(personagem3, (30, 30))
quest = pygame.image.load('noz.png')
questImg = pygame.transform.scale(quest, (60, 60))
cenario = pygame.image.load('base.png')
DEFAULT_CENARIO_SIZE = (400, 600)
cenario=pygame.transform.scale(cenario,DEFAULT_CENARIO_SIZE)
tela = pygame.display.set_mode((largura_janela, altura_janela))
x = (largura_janela * 0.1)
y = (altura_janela * 0.1)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
personagem_speed = 0
xesquilo = x+35
yesquilo = y+35
xnuvem = 40+35 #500
ynuvem = 40+35 #400
xnuvem1 = 20+40 #500
ynuvem1 = 150+40 #400
xnoz = 21 + 35
ynoz = 21 + 35
x_1 = x
y_1 = y

#definição de colisão e balão de falas

def colidiu():
    distancia =  math.sqrt(math.pow(xesquilo-xnuvem,2)+math.pow(yesquilo-ynuvem,2))
    print (distancia)
    if distancia<=20:
        return True
    else:
        return False

def colidiu2():
    distancia =  math.sqrt(math.pow(xesquilo-xnoz,2)+math.pow(yesquilo-ynoz,50))
    if distancia<=35+21:
        return True
    else:
        return False

def colidiu3():
    distancia =  math.sqrt(math.pow(xesquilo-xnoz,14)+math.pow(yesquilo-ynoz,14))
    if distancia<=50+50:
        return True
    else:
        return False

def balao(screen,text, x0,y0):
    font = pygame.font.SysFont('comicsansms', 12, bold=False, italic=False)  #pygame.font.Font(font, 12)
    textSurf = font.render(text, True, (30,30,30)).convert_alpha()
    textSize = textSurf.get_size()   
    bubbleSurf = pygame.Surface((textSize[0] + 31, textSize[1] + 15 + 30))
    bubbleSurf.fill((0,0,0))
    bubbleSurf.set_colorkey((0,0,0))  
    l = 6
    x,y = textSize[0] + 30, textSize[1] + 15
    points = [ [l,0], [x-l,0],[x,l],[x,y-l],[x-l,y], [x/2+6,y] ,[x/2,y+30], [x/2-6,y] ,[l,y],[0,y-l],[0,l]]
    pygame.draw.polygon(bubbleSurf, (255,255,255), points)
    pygame.draw.lines(bubbleSurf, (30,30,30), True, points)
    bubbleRect = bubbleSurf.get_rect()
    bubbleSurf.blit(textSurf, textSurf.get_rect(center = (x/2,y/2)))
    bubbleRect.center = (x0,y0-bubbleRect[3]/2)
    screen.blit(bubbleSurf, bubbleRect)

# Funções de colisão para cada nuvem
def colidiu_nuvem1():
    distancia = math.sqrt(math.pow(xesquilo- -25, 2) + math.pow(yesquilo - 250, 2))
    if distancia <= 70+35 :
        return True
    else:
        return False

def colidiu_nuvem2():
    distancia = math.sqrt(math.pow(xesquilo -500, 2) + math.pow(yesquilo - 500, 2))
    if distancia <= 20:
        return True
    else:
        return False

def colidiu_nuvem3():
    distancia = math.sqrt(math.pow(xesquilo - 250, 2) + math.pow(yesquilo - 460, 2))
    if distancia <= 20:
        return True
    else:
        return False

def colidiu_nuvem4():
    distancia = math.sqrt(math.pow(xesquilo - 250, 2) + math.pow(yesquilo - 460, 2))
    if distancia <= 20:
        return True
    else:
        return False

def colidiu_nuvem5():
    distancia = math.sqrt(math.pow(xesquilo - 250, 2) + math.pow(yesquilo - 460 , 2))
    if distancia <= 20:
        return True
    else:
        return False

def colidiu_nuvem6():
    distancia = math.sqrt(math.pow(xesquilo - 250, 2) + math.pow(yesquilo - 460, 2))
    if distancia <= 20:
        return True
    else:
        return False

def colidiu_nuvem7():
    distancia = math.sqrt(math.pow(xesquilo - 250, 2) + math.pow(yesquilo - 460, 2))
    if distancia <= 20:
        return True
    else:
        return False

def colidiu_nuvem8():
    distancia = math.sqrt(math.pow(xesquilo - 250, 2) + math.pow(yesquilo - 460, 2))
    if distancia <= 50:
        return True
    else:
        return False

def colidiu_nuvem9():
    distancia = math.sqrt(math.pow(xesquilo - 250, 2) + math.pow(yesquilo - 460, 2))
    if distancia <= 50:
        return True
    else:
        return False

def colidiu_nuvem10():
    distancia = math.sqrt(math.pow(xesquilo - 250, 2) + math.pow(yesquilo - 460, 2))
    if distancia <= 50 + 50:
        return True
    else:
        return False




while not fgExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
        if event.type == pygame.MOUSEBUTTONDOWN and colidiu() == True and colidiu3()== False:
            pass
        if colidiu2():
            xnoz = xesquilo - 35
            ynoz = yesquilo - 35
            personagem3Img = pygame.transform.scale(personagem3, (21, 21))

        if event.type == pygame.MOUSEBUTTONDOWN and colidiu3() == True: 

            pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x2 = 0
            if event.key == pygame.K_UP:
                y1 = 0
            if event.key == pygame.K_DOWN:
                y2 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -5
            if event.key == pygame.K_RIGHT:
                x2 = 5
            if event.key == pygame.K_UP:
                y1 = -5
            if event.key == pygame.K_DOWN:
                y2 = 5


    x += x1 + x2
    y += y1 + y2
    xesquilo = x+45
    yesquilo = y+65
    if colidiu():
        print ('colisão entre o esquilo e a nuvem')
    if colidiu2():
        print('colisão entre o esquilo e a noz')
    if colidiu():
        print('colisão entre a esquilo e a nuvem')

    # Verificação de colisões com as nuvens
    if colidiu_nuvem1():
        print("Colisão com nuvem 1!")
        fgExit = True  # Termina o jogo
    if colidiu_nuvem2():
        print("Colisão com nuvem 2!")
        fgExit = True
    if colidiu_nuvem3():
        print("Colisão com nuvem 3!")
        fgExit = True
    if colidiu_nuvem4():
        print("Colisão com nuvem 4!")
        fgExit = True
    if colidiu_nuvem5():
        print("Colisão com nuvem 5!")
        fgExit = True
    if colidiu_nuvem6():
        print("Colisão com nuvem 6!")
        fgExit = True
    if colidiu_nuvem7():
        print("Colisão com nuvem 7!")
        fgExit = True
    if colidiu_nuvem8():
        print("Colisão com nuvem 8!")
        fgExit = True
    if colidiu_nuvem9():
        print("Colisão com nuvem 9!")
        fgExit = True
    if colidiu_nuvem10():
        print("Colisão com nuvem 10!")
        fgExit = True

#exibição na tela dos personagens 

    tela.blit(cenario,(0,0))
    tela.blit(questImg, (520, 130))
    tela.blit(nuvem1Img, (20, 150))
    tela.blit(nuvem2Img, (20, 280))
    tela.blit(nuvem3Img, (20, 450))
    tela.blit(nuvem4Img, (150, 80))
    tela.blit(nuvem5Img, (160, 230))
    tela.blit(nuvem6Img, (150, 360))
    tela.blit(nuvem7Img, (270, 0))
    tela.blit(nuvem8Img, (270, 150))
    tela.blit(nuvem9Img, (270, 280))
    tela.blit(nuvem10Img, (270, 360))
    tela.blit(personagemImg, (x + 250, y + 460))
    tela.blit(personagem3Img, (60, 35))


    pygame.display.update()
    clock.tick(60)



pygame.quit()