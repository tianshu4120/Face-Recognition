import pygame
import pygame.camera
from pygame.locals import *
 
pygame.init()
pygame.camera.init()
 
camera = pygame.camera.Camera("/dev/video0",(640,480))
camera.start()
image = camera.get_image()
pygame.image.save(image,"image.png")
camera.stop()
