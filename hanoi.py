import pygame
import sys
import time
from pygame.locals import*
pygame.init()

#cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (80, 0, 0)
gold = (218, 165, 32)
blue = (78,162,196) 
grey = (26, 25, 24)
green = (77, 206, 145)
bordo = (111, 9, 0)

#definindo variáveis
apontando=0
se_mexendo = False
numero_discos=3
discos=[]
movimentos=0
#definindo funções
def sombras(tela, text, midtop, size, s_color=red):
    x=[]
    for elem in midtop:
        x.append(elem)
    fonte=pygame.font.get_default_font()
    fonte_padrao=pygame.font.SysFont(fonte, size)
    fonte_printar=fonte_padrao.render(text, 1, s_color)
    fonte_area=fonte_printar.get_rect()
    fonte_area.midtop=(x[0]+3, x[1]+3)
    tela.blit(fonte_printar, fonte_area)
    
def printar_texto(tela, text, midtop, size=None, color=None): #função para printar texto
    fonte=pygame.font.get_default_font()
    fonte_padrao=pygame.font.SysFont(fonte, size)
    fonte_printar=fonte_padrao.render(text, 1, color)
    fonte_area=fonte_printar.get_rect()
    fonte_area.midtop=midtop
    sombras(tela, text, midtop, size, s_color=red)
    tela.blit(fonte_printar, fonte_area)

def mk_discos(numero_discos, discos): #função para criar os discos
    altura=20
    largura=numero_discos*23
    x=120-largura+(largura/2)
    y=400 - altura
    for elem in range(numero_discos):
        discos_d={} #cria um dicionario vazio
        discos_d['area']= pygame.Rect(0, 0, largura, altura)
        discos_d['area'].midtop=(120, y) #define a area do disco
        discos_d['tamanho']=numero_discos-elem #define o tamanho do disco para a comparação
        discos_d['torre']=0 #define qual torre o disco vai ir
        discos.append(discos_d) #armazena o dicionário numa lista
        largura-=23 #diminui o tamanho do disco
        y-=altura+3 #coloca uma margem entre um disco e outro
        
pygame.display.set_caption("Torre de Hanoi")
tela = pygame.display.set_mode((640, 480)) #cria a tela principal
menu_fechar=False
while not menu_fechar:
    tela.fill(bordo) #preenche a tela de preto
    printar_texto(tela, 'Torre de Hanoi', (320, 110), size=60, color=gold)
    printar_texto(tela, 'Pressione ENTER para continuar', (320, 180), size=30, color=white)
    printar_texto(tela, 'Use as setas para selecionar o número de discos', (320, 250), size=30, color=white)
    printar_texto(tela, str(numero_discos), (320, 300), size=30, color=gold)
    printar_texto(tela, 'hanoi.py - 04/07/2019 - vmvr', (320, 460), size=18, color=white)
    for event in pygame.event.get(): #verifica os eventos do teclado do usuário
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #inicia o jogo
                    jogo_acabou=False
                    menu_fechar=True
                if event.key == pygame.K_UP: #aumenta o numero de discos
                    numero_discos+=1
                    if numero_discos > 6:
                        numero_discos=6
                if event.key == pygame.K_DOWN: #diminui o numero de discos
                    numero_discos-=1
                    if numero_discos < 1:
                        numero_discos=1
    pygame.display.update() #atualiza a tela
def des_torres(): #desenha as torres
        pygame.draw.rect(tela, black, [45, 400, 149, 20]) #torre 1
        pygame.draw.rect(tela, grey, [115, 250, 12, 150])

        pygame.draw.rect(tela, black, [245, 400, 149, 20]) #torre 2
        pygame.draw.rect(tela, grey, [315, 250, 12, 150])
        
        pygame.draw.rect(tela, black, [445, 400, 149, 20]) #torre 3
        pygame.draw.rect(tela, grey, [515, 250, 12, 150])
        return
torres_x=[120, 320, 520] #guarda a posição das torres
def desenhar(): #desenha os discos
        global tela
        global discos
        for discos_d in discos:
            pygame.draw.rect(tela, gold, discos_d['area'])
        return
def seta(): #define o cursor (seta)
    global apontando
    setinha=[(torres_x[apontando]-7, 440), (torres_x[apontando]+7, 440), (torres_x[apontando], 433)]
    pygame.draw.polygon(tela, gold, setinha)
    return
def acabou():
    global tela
    global movimentos
    global numero_discos
    global jogo_acabou
    jogo_acabou=True
    tela.fill(bordo)
    minimos=2**numero_discos-1
    printar_texto(tela, 'Você ganhou!', (320, 150), size=72, color=gold)
    printar_texto(tela, 'Seus movimentos: '+str(movimentos), (320, 250), size=30, color=white)
    printar_texto(tela, 'Movimentos mínimos: '+str(minimos), (320, 320), size=30, color=white)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    sys.exit()
def ganhou():
    global discos
    ganhou=True
    for discos_d in discos:
        if discos_d['torre']!=2:
            ganhou=False
    if ganhou:
        time.sleep(0.2)
        acabou()
mk_discos(numero_discos, discos)
while not jogo_acabou:
    tela.fill(bordo) #limpa a tela
    seta()
    for event in pygame.event.get(): #analisa os eventos do teclado
        if event.type==pygame.QUIT:
            jogo_acabou=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT: #move o cursor para a direita
                apontando+=1
                if apontando==3:
                    apontando=0
                if se_mexendo: #se tiver se mexendo, move o disco pra direita
                    discos[disco_mexendo]['area'].midtop=(torres_x[apontando], 100)
                    discos[disco_mexendo]['torre']=apontando
            if event.key==pygame.K_LEFT: #move o cursor para a esquerda
                apontando-=1
                if apontando==-1:
                    apontando=2
                if se_mexendo: #se tiver se mexendo, move o disco pra esquerda
                    discos[disco_mexendo]['area'].midtop=(torres_x[apontando],100)
                    discos[disco_mexendo]['torre']=apontando
            if event.key==pygame.K_UP and not se_mexendo:
                for discos_d in discos[::-1]: #pega o primeiro disco (último a ser criado) - PILHA
                    if discos_d['torre']==apontando:
                        se_mexendo=True
                        disco_mexendo=discos.index(discos_d)
                        discos_d['area'].midtop=(torres_x[apontando],100) #define as posições de x e y para o disco
                        break
            if event.key==pygame.K_DOWN and se_mexendo: #se tiver se mexendo, ele volta o disco pra torre
                for discos_d in discos[::-1]:
                    if discos_d['torre']==apontando and discos.index(discos_d)!=disco_mexendo: #o disco da torre deve ser diferente do disco se mexendo
                        if discos_d['tamanho']>discos[disco_mexendo]['tamanho']: #verifica se a jogada é válida
                            se_mexendo=False
                            discos[disco_mexendo]['area'].midtop=(torres_x[apontando], discos_d['area'].top-23)
                            movimentos+=1
                            break
                        else:
                            discos[disco_mexendo]['area'].midtop=(torres_x[apontando], 100)
                            break
                else:
                    se_mexendo=False
                    discos[disco_mexendo]['area'].midtop=(torres_x[apontando], 380)
                    movimentos+=1

    tela.fill(bordo)
    des_torres()
    desenhar()
    seta()
    printar_texto(tela, 'Movimentos: '+str(movimentos), (320, 20), size=30, color=white)
    pygame.display.update()
    if not se_mexendo: ganhou()
    
                    
                

