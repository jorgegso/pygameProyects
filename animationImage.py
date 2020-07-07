import pygame


#colores

NEGRO      =   (   0,   0,   0)
BLANCO     =   ( 255, 255, 255)
VERDE      =   (   0, 255,  0)
ROJO       =   ( 255,  0,  0)
MARRON     =   ( 219,139,  9) 
MARRONCLARO  = ( 186,173,32 )
ASUL         = ( 191,242,240)
AMARILLO     = ( 237,229,7  )
VERDEPASTO   = (  22,189,4  )
VIOLETA   =    ( 98 ,  0,255)
pygame.init()
#init





tamano = (800, 900)# largo altura
pantalla = pygame.display.set_mode(tamano)

pygame.display.set_caption("Mi dibujo")#conesto le damos un titulo



#aqui comiensa el loop
terminar = False

reloj = pygame.time.Clock()

movete_oja = 0
buelve = 1
altura = 0
alturalimite = -1
muevetenube = 0
nubeincremento = 1
bajanuve = 1
alturanuve = 0
inclementonube2 = 1
tiemposemaforo = 0
incrementocemaforo = 1
while not terminar:
    for evento in pygame.event.get(): #el usuario iso algo
        if evento.type == pygame.QUIT: 
            terminar = True 
            
    
    pantalla.fill(BLANCO) #despues de esto
  
    
    pygame.draw.rect(pantalla, ASUL , [0,0,800,800] )#SIELO
    pygame.draw.ellipse(pantalla,AMARILLO,[670,-60,200,200])#SOL
    for nubes in range(1,800,200):
        pygame.draw.ellipse(pantalla,BLANCO,[580-nubes + muevetenube*2,50 + alturanuve  ,100 ,101])#nubes
        pygame.draw.ellipse(pantalla,BLANCO,[625-nubes + muevetenube*2,50 + alturanuve ,100,100])
        pygame.draw.ellipse(pantalla,BLANCO,[600-nubes + muevetenube*2,130 + alturanuve ,107,100])
        pygame.draw.ellipse(pantalla,BLANCO,[635-nubes + muevetenube*2,100 + alturanuve,100,90])        
        pygame.draw.ellipse(pantalla,BLANCO,[560-nubes + muevetenube*2,100 + alturanuve ,100,90])
        
        pygame.draw.ellipse(pantalla,BLANCO,[600,90,50,50])#nubes
        pygame.draw.ellipse(pantalla,BLANCO,[625-nubes,50,100,100])
        pygame.draw.ellipse(pantalla,BLANCO,[500-nubes,50,100,90])
        pygame.draw.ellipse(pantalla,BLANCO,[635-nubes,100,90,90])        
        pygame.draw.ellipse(pantalla,BLANCO,[560-nubes,100,90,90])
        
    alturanuve += inclementonube2  
    muevetenube += nubeincremento 
    if muevetenube == 50:
        nubeincremento  = -1
        bajanuve = -1 
    elif muevetenube == -60:
        nubeincremento = 1 
        bajanuve = 1 
        
    if alturanuve == 44:
        inclementonube2 = -1
    elif alturanuve == -40:
        inclementonube2 = 1 
        
    pygame.draw.rect(pantalla, MARRON , [80,180,500,600])#cabessa
    for pelomoviendoce in range(0,520,20):
        pygame.draw.line(pantalla, MARRONCLARO, [80+pelomoviendoce,180], [80+pelomoviendoce,780], 6)#cabellos
        
    pygame.draw.polygon(pantalla,ROJO,[[330,0],[582,180],[77,180]])#TECHO 
    
    pygame.draw.rect(pantalla, MARRON, [135,270,130,150],16)#ventana
    pygame.draw.rect(pantalla, BLANCO, [135,270,130,150]) 
    
    
           
    pygame.draw.rect(pantalla, MARRON, [380,270,130,150],16 )#ventana
    pygame.draw.rect(pantalla,BLANCO , [380,270,130,150])#ventanafondo
    if tiemposemaforo < 15:
        pygame.draw.rect(pantalla,NEGRO , [380,270,130,150])
    elif tiemposemaforo > 30:
        pygame.draw.rect(pantalla,NEGRO , [380,270,130,150])
    if tiemposemaforo == 90:
        incrementocemaforo = -1 
    elif tiemposemaforo == 0:
        incrementocemaforo = 1
        
    tiemposemaforo += incrementocemaforo  
    
    pygame.draw.rect(pantalla, MARRONCLARO, [166+80,480,150,300])
    pygame.draw.rect(pantalla, MARRON , [246,480,150,300],5)#puerta
    pygame.draw.rect(pantalla, VERDEPASTO, [0,780,800,110] )#PASTO
    
    for repeticion in range (0,750,30):
        pcirculox = (10 + movete_oja  ) + repeticion
        pcirculoy = 800 + altura        
        
        pygame.draw.line(pantalla, VERDE , [pcirculox , pcirculoy  ], [50 + repeticion ,850], 5) #tallo
        pygame.draw.ellipse(pantalla,VIOLETA,[pcirculox -10 ,  pcirculoy -10 ,20,20])#flor     
    
    movete_oja += buelve  
    altura += alturalimite
    if movete_oja == 80:
        buelve = - 1 
    elif movete_oja == -1:
        buelve = 1 
    if altura  == -10: #altura  == -100
        alturalimite = 2
    elif altura == 20:#altura == 10
        alturalimite = -2
    
    
    pygame.display.flip()
    reloj.tick(20)
pygame.quit()    
    
    
  
     
