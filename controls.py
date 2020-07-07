import pygame
from math import pi

def crear_auricular(pantalla , x, y ):
    pygame.draw.circle(pantalla, ROJO , [ 350 - 275 + x, 150 - 75  + y], 40, )#cabesa
    pygame.draw.circle(pantalla, GRIS , [410 - 275 + x, 150 - 75 + y], 25 )#isquierdo    
    pygame.draw.circle(pantalla, GRIS , [  290 - 275 + x, 150 - 75  + y], 25 )#derecho
    pygame.draw.arc(pantalla, GRIS ,[  275 - 275+ x , 75 - 75 + y, 150, 125], 0 , pi/1 , 8)#curba    
    pygame.draw.arc(pantalla, NEGRO, [325 - 275 + x, 160 - 75  + y, 50, 15], pi,4*pi/2, 4)#SONRRIZA    
    pygame.draw.circle(pantalla, AZUL , [ 330 - 275 + x,  140 - 75  + y], 9) #hojos
    pygame.draw.circle(pantalla, AZUL , [365 - 275 + x , 140  - 75 + y], 9)#hojos    
def crear_gusanito(pantalla , x , y ):
    xa = 0
    VELOCIDAD = 0    
    for i in range (8):         
        pygame.draw.circle(pantalla, NARANJA, [ 200 + VELOCIDAD + x - 192,  400 + y - 397], 10 - xa)
        VELOCIDAD += 12
        xa +=1
    pygame.draw.circle(pantalla, BLANCO, [ 197  + x - 192,  397 + y - 397], 3 )
    pygame.draw.circle(pantalla, BLANCO, [ 192  + x - 192,  405 + y - 397], 3 )    

NEGRO    = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
AZUL     = (  9,   197, 141)
VERDE    = (   0, 255,   0)
ROJO      = ( 255,   0,   128)
GRIS     = ( 132,   132,   132)
NARANJA = (255,123,0)
dimenciones = (600,800)

pantalla = pygame.display.set_mode(dimenciones) #dimenciones
pygame.display.set_caption("juego con controles ")

done = False
reloj = pygame.time.Clock()

pygame.mouse.set_visible(False)#no se ve el mouse

x_velocidad = 0
y_velocidad = 0
   
pisicion_x = 10
pisicion_y = 10 




while not done:
    for evento in pygame.event.get():
                  
        if evento.type == pygame.QUIT: 
            done = True
        if evento.type == pygame.KEYDOWN:# tecla arriba 
                   
                   
            if evento.key == pygame.K_LEFT:
                x_velocidad = -5
            if evento.key == pygame.K_RIGHT:
                x_velocidad = 5
            if evento.key == pygame.K_UP:
                y_velocidad = -5
            if evento.key == pygame.K_DOWN:
                y_velocidad = 5          
                
        if evento.type == pygame.KEYUP: # tecla abajo
            
            if evento.key == pygame.K_LEFT:
                x_velocidad = 0
            if evento.key == pygame.K_RIGHT:
                x_velocidad = 0
            if evento.key == pygame.K_UP:
                y_velocidad = 0
            if evento.key == pygame.K_DOWN:
                y_velocidad = 0                    
            
                
           
            
   # no puede salire del recuadro 
        
    if pisicion_x  <= 0:
        pisicion_x = 600 
    if pisicion_x >= 600:
        pisicion_x = 0 
    if pisicion_y >= 800:
        pisicion_y = 0 
    if pisicion_y < 0:
        pisicion_y = 800     
    # no puede salire del recuadro 
    
    
    pisicion_x  += x_velocidad
    pisicion_y  += y_velocidad                          
                          
                          
    pos = pygame.mouse.get_pos()
    x = pos[0]#(666,777)
    y = pos[1]         
                                  
    pantalla.fill(BLANCO)
    
         
    crear_auricular(pantalla , x, y )
    crear_auricular(pantalla , 899, 34)
    crear_auricular(pantalla , 78, 5 )
    
    crear_gusanito(pantalla , pisicion_x , pisicion_y)
    crear_gusanito(pantalla , 567 , 198)
    crear_gusanito(pantalla , 34 , 56)
  
    pygame.display.flip()
    reloj.tick(60)
    
    
pygame.quit()

