import pygame
file_name = 'C:\\Users\\pedro\\Downloads\\msc.mp3'
pygame.init()
pygame.mixer.init()
musica = str(input('Digite música boa: '))
if musica == 'musica boa': 
    s = pygame.mixer.Sound(file_name)
    s.play()
    s.set_volume(0.1)
    input('música boa')
    
