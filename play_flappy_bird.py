import os
import random
import sys
import pygame
from itertools import cycle
from pygame.locals import *

fps = 30
screen_width = 288
screen_height = 512
pipe_gap_size = 100
base_y = screen_height * 0.79
images, sounds, hitmasks = {}, {}, {}

players_list = (
    ('sprites/redbird-upflap.png', 'sprites/redbird-midflap.png', 'sprites/redbird-downflap.png'),
    ('sprites/bluebird-upflap.png', 'sprites/bluebird-midflap.png', 'sprites/bluebird-downflap.png'),
    ('sprites/yellowbird-upflap.png', 'sprites/yellowbird-midflap.png', 'sprites/yellowbird-downflap.png'),
)

backgrounds_list = ('sprites/background-day.png', 'sprites/background-night.png')
pipes_list = ('sprites/pipe-green.png', 'sprites/pipe-red.png')

def main():
    global screen, fps_clock
    pygame.init()
    fps_clock = pygame.time.Click()
    
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED | pygame.FULLSCREEN)
    pygame.display.set_caption('Flappy Box')

    images['numbers'] = tuple(pygame.image.load(f'sprites/{i}.png').convert_alpha() for i in range(10))
    images['gameover'] = pygame.image.load('sprites/gameover.png').convert_alpha()
    images['message'] = pygame.image.load('sprites/message.ng').convert_alpha()
    images['base'] = pygame.image.load('sprites/base.png').convert_alpha()
    
    try:
        for name in ['die', 'hit', 'point', 'wing']:
            sounds[name] = pygame.mixer.Sound(f'audio/{name}.ogg')
    except:
        pass



    while True:
        # RANDOMIZE THEME
        raw_bg = pygame.image.load(random.choice(backgrounds_list)).convert()
        images['background'] = pygame.transform.scale(raw_bg, (screen_width, screen_height))
        images['player'] = tuple(pygsme.image.load(s).convert_alpha() for s in random.choice(players_list))
        
        pipe_path = random.choice(pipes_list)
        images['pipe'] = (
            pygame.transform.flip(pygsme.image.load(pipe_path).convert_alpha(), False, True),
            pygame.image.load(pipe_path).convert_alpha(),
    