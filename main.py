# -*- coding=utf-8 -*-
import pygame
from pygame.locals import KEYDOWN
import random

w,h = 800,600
pygame.init()
screen = pygame.display.set_mode((w, h))

white=255,255,255
black=0,0,0
myfont = pygame.font.Font(None,80)

diff_ticks = 20
ticks = pygame.time.get_ticks() + diff_ticks
word_diff_ticks = diff_ticks * 50
word_ticks = pygame.time.get_ticks() + word_diff_ticks

def get_random_word():
    c = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    return random.randint(100, w-100),0,random.randint(65, 90),c
arr=[]
arr.append(get_random_word())
game_state=1
clear_word=0
level = 1
pygame.display.set_caption('typing level:%d'%level)
sign=1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_state==1 and len(arr)>0 and event.type == KEYDOWN:
            if event.key == arr[0][2]+32:
                arr.pop(0)
                clear_word += 1
                if clear_word >= level*10:
                    level+=1
                    pygame.display.set_caption('typing level:%d' % level)
                    diff_ticks=diff_ticks*0.9
                    word_diff_ticks=word_diff_ticks*0.95

    screen.fill((255, 255, 255))

    for i in range(len(arr)):
        x, y, word, c = arr[i]
        if i==0 and sign:
            c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))\

        textImage = myfont.render(chr(word), True, c)
        screen.blit(textImage, (x, y))

    if game_state == 2:
        textImage = myfont.render("Level%d fail"%level, True, (255,0,0))
        sw,sh = textImage.get_size()
        screen.blit(textImage, ((w-sw)/2, (h-sh)/2))

    if game_state == 1:
        if pygame.time.get_ticks() >= ticks:
            ticks += diff_ticks
            sign=1-sign
            for i in range(len(arr)):
                x, y, word, c = arr[i]
                arr[i] = (x, y+1, word, c)
            if len(arr) > 0 and arr[0][1] > h: game_state=2
        if pygame.time.get_ticks()>=word_ticks:
            word_ticks +=word_diff_ticks
            arr.append(get_random_word())

    pygame.display.update()
