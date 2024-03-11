import sys
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 640
largura = 640
x= largura/2
y= altura/2
D=150
c=50
isjump=False
v=5
m=10

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('inject')
clock=pygame.time.Clock()
ret_red=pygame.draw.rect(tela, ('red'),(x,y,50,50))
chao=pygame.draw.rect(tela,('green'),(0,500,640,50))


while True:
    y=y+5
    D=D+3
    
    clock.tick(10)
    tela.fill(('yellow'))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
       #''' if ret_red.colliderect(chao):  
         # if event.type == KEYDOWN:
           # if event.key == K_w:'''
              
    if isjump==False:
      if ret_red.colliderect(chao):   
        if pygame.key.get_pressed() [K_w]:
          isjump=True
          
    if isjump:
      F= (1/2)*m*(v**2)
      y-=F
      
      v=v-1
      if v<0:
        m=-2
    if v==-9:
      isjump=False
      v=5
      m=10
        

    if pygame.key.get_pressed()[K_a]:
      x=x-10
    if pygame.key.get_pressed()[K_d]:
      x=x+10  
    if pygame.key.get_pressed()[K_s]:
      y=y+10
    p,o = pygame.mouse.get_pos()
    mouse= pygame.draw.circle(tela,('black'),(p,o),10)
    ret_red=pygame.draw.rect(tela, ('red'),(x,y,50,50))
    ret_yl=pygame.draw.rect(tela,('pink'),(100,D,50,c))
    chao=pygame.draw.rect(tela,('green'),(0,500,640,50))
  
    if ret_red.colliderect(ret_yl):
      c=0

    if ret_red.colliderect(chao):
      y=450

    if ret_yl.colliderect(chao):
      D=450

  
    
    pygame.display.update()