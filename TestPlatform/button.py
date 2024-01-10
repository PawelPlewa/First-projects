import pygame as pg


class Button(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, game, colour='green'):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.clicked = False

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.collidepoint(self.game.pos):
            self.image.fill('#20c420')
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        else:
            self.image.fill(self.colour)

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False