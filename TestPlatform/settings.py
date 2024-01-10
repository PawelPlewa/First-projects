import pygame


TITLE = 'CAPITALS GAME, FUN'
WIDTH = 600
HEIGHT = 600

FPS = 60
colours = {
    'green': (0, 255, 0),
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255),
    'beer': (251, 177, 23)
}
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
gui_font = pygame.font.Font(None, 30)


TRIGONOMETRY = {
    'sin0': 0,
    'cos0': 1,
    'tg0': 0,
    'ctg0': '---',

    'sin90': 1,
    'cos90': 0,
    'tg90': '---',
    'ctg90': 0,

    'sin180': 0,
    'cos180': -1,
    'tg180': 0,
    'ctg180': '---',

    'sin270': -1,
    'cos270': 0,
    'tg270': '---',
    'ctg270': 0,

    'sin360': 0,
    'cos360': 1,
    'tg360': 0,
    'ctg360': '---',

    'sin(-α)': '-sinα',
    'cos(-α)': 'cosα',
    'tg(-α)': '-tgα',
    'ctg(-α)': '-ctgα',

    'sin(90-α)': 'cosα',
    'cos(90-α)': 'sinα',
    'tg(90-α)': 'ctgα',
    'ctg(90-α)': 'tgα',

    'sin(90+α)': 'cosα',
    'cos(90+α)': '-sinα',
    'tg(90+α)': '-ctgα',
    'ctg(90+α)': '-tgα',

    'sin(180-α)': 'sinα',
    'cos(180-α)': '-cosα',
    'tg(180-α)': '-tgα',
    'ctg(180-α)': '-ctgα',

    'sin(180+α)': '-sinα',
    'cos(180+α)': '-cosα',
    'tg(180+α)': 'tgα',
    'ctg(180+α)': 'ctgα',

    'sin(270-α)': '-cosα',
    'cos(270-α)': '-sinα',
    'tg(270-α)': 'ctgα',
    'ctg(270-α)': 'tgα',

    'sin(270+α)': '-cosα',
    'cos(270+α)': 'sinα',
    'tg(270+α)': '-ctgα',
    'ctg(270+α)': '-tgα',

    'sin(360-α)': '-sinα',
    'cos(360-α)': 'cosα',
    'tg(360-α)': '-tgα',
    'ctg(360-α)': '-ctgα',

    'sin(360+α)': 'sinα',
    'cos(360+α)': 'cosα',
    'tg(360+α)': 'tgα',
    'ctg(360+α)': 'ctgα',
}

FUNCS = ['sin0', 'cos0', 'tg0', 'ctg0', 'sin90', 'cos90', 'tg90', 'ctg90', 'sin180', 'cos180', 'tg180', 'ctg180',
         'sin270', 'cos270', 'tg270', 'ctg270', 'sin360', 'cos360', 'tg360', 'ctg360', 'sin(-α)', 'cos(-α)', 'tg(-α)',
         'ctg(-α)', 'sin(90-α)', 'cos(90-α)', 'tg(90-α)', 'ctg(90-α)', 'sin(90+α)', 'cos(90+α)', 'tg(90+α)','ctg(90+α)',
         'sin(180-α)', 'cos(180-α)', 'tg(180-α)', 'ctg(180-α)', 'sin(180+α)', 'cos(180+α)', 'tg(180+α)', 'ctg(180+α)',
         'sin(270-α)', 'cos(270-α)', 'tg(270-α)', 'ctg(270-α)', 'sin(270+α)', 'cos(270+α)', 'tg(270+α)', 'ctg(270+α)',
         'sin(360-α)', 'cos(360-α)', 'tg(360-α)', 'ctg(360-α)', 'sin(360+α)', 'cos(360+α)', 'tg(360+α)', 'ctg(360+α)']