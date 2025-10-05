import pygame
import pyautogui
from PIL import Image
from PIL import *
import json


pygame.init()
running = True
display = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
frame = 0
delta = 0
time = 0
fps = 60
screenshot = pyautogui.screenshot(region=(0, 70, 1920, 1080))
screenshot.save('screenshot.png', 'png')
image = pygame.image.load('screenshot.png')
movie_image = []
with open('Movie.json', 'r') as m:
    data = json.load(m)
    images = data["images"]
    for i in images:
        movie_image.append(pygame.image.load(i))
movie_fps = 0.1

while running:
    display.blit(image, (0, 0))

    print(" mfps " + str(movie_fps) + " fps " + str(fps) + " mfps/fps " + str(movie_fps/fps) + " frame" + str(frame) + " movie_fps/fps*frame "+ str(movie_fps/fps*frame) + " image_movie " + str(movie_image[int(movie_fps/fps*frame)]))
    display.blit(movie_image[int(movie_fps/fps*frame)], (0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(fps)
    frame += 1
    delta = clock.get_rawtime()
    time += delta


pygame.quit()