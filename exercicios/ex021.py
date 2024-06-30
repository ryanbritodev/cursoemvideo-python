import pygame
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
print("Reproduzindo música...")
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
