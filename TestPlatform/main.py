# import urllib.request
# import re

# get url as str
# fp = urllib.request.urlopen("https://pl.wikipedia.org/wiki/Stolice_pa%C5%84stw_%C5%9Bwiata")
# my_bytes = fp.read()
# page_Str = my_bytes.decode('utf-8')
# fp.close()
#
#
# # regular expression
# href = '<a href="/wiki/[_\\-a-zA-Z0-9%]+" title="([^"]+)+">[^<]+</a>'
# r = re.findall(f'<tr>\s*<td>\s*{href}\s*</td>\s*<td>\s*{href}\s*(<sup [^>]+>\s*.+\s*</sup>\s*<br\s*/?>\s*)?({href})?', page_Str)
#
# wyniki = []
# for k in r:
#     # print if not empty and isn't some strange html
#     wyniki.append(list(filter(lambda place: len(place) > 0 and place.find('>')==-1, k)))
#
# s = json.dumps(wyniki)
# f = open('stolice.json', 'w')
# f.write(s)
# f.close()


import json
import random
import time
from button import *
from settings import *


# we use json cuz it is fun
s = open('stolice.json').read()
data = json.loads(s)

# make a dict country: capital(s)
data_dict = {}
data_countries = list()
for d in data:
    data_dict[d[0]] = d[1:]
    data_countries.append(d[0])
pg.init()


class Game:
    MODE = None
    def __init__(self):
        # init pygame
        pg.init()
        self.running = True
        self.playing = True

        # window and FPS control
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        self.font = pg.font.match_font('arial black')

    def new(self):
        # we set our gamemode, take the right data
        if self.mode == 'geography':
            self.INDEXES_ANSWERS = data_dict
            self.take_data = data_countries
            self.repeatable = False
        elif self.mode == 'trigonometry':
            self.INDEXES_ANSWERS = TRIGONOMETRY
            self.take_data = FUNCS
            self.repeatable = True

        # properties of the game
        self.points = 0
        self.mistakes = 0
        self.task = random.choice(self.take_data)
        self.solution = self.INDEXES_ANSWERS[self.task]
        if self.repeatable:
            self.possible_set = list(set(self.INDEXES_ANSWERS.values()))
        else:
            self.possible_set = list(self.INDEXES_ANSWERS.values())

        # incorrect answers taken from a set of possible solutions
        self.possible_set.remove(self.solution)
        self.wrong = random.sample(self.possible_set, 1)[0]
        self.possible_set.remove(self.wrong)
        self.wrong2 = random.sample(self.possible_set, 1)[0]
        if self.repeatable:
            self.possible_set = list(set(self.INDEXES_ANSWERS.values()))
        else:
            self.possible_set = list(self.INDEXES_ANSWERS.values())

        self.answers = [self.solution, 0, 0]

        self.points = 0
        # sprite groups
        self.all_sprites = pg.sprite.Group()
        self.buttons = pg.sprite.Group()

        # create all the buttons
        self.exit_button = Button(WIDTH/2, HEIGHT-50, 190, 100, self, '#8d021f')

        self.answer_button1 = Button(100, HEIGHT-400, 150, 100, self, '#003d80')
        self.answer_button2 = Button(300, HEIGHT - 400, 150, 100, self, '#003d80')
        self.answer_button3 = Button(500, HEIGHT - 400, 150, 100, self, '#003d80')

        self.restart_button = Button(WIDTH-60, HEIGHT-50, 120, 100, self, '#3a3a3a')
        # places where we put our text
        self.variations = [self.answer_button1.rect.centerx,
                           self.answer_button2.rect.centerx,
                           self.answer_button3.rect.centerx]
        self.place = random.choice(self.variations)

        self.all_sprites.add(self.exit_button)
        self.all_sprites.add(self.answer_button1)
        self.all_sprites.add(self.answer_button2)
        self.all_sprites.add(self.answer_button3)
        self.all_sprites.add(self.restart_button)

        self.buttons.add(self.exit_button)
        self.buttons.add(self.answer_button1)
        self.buttons.add(self.answer_button2)
        self.buttons.add(self.answer_button3)
        self.buttons.add(self.restart_button)

        # run the game
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.update()
            self.draw()
            self.events()

    def update(self):
        self.pos = pg.mouse.get_pos()
        self.all_sprites.update()

        if self.task is not None:
            self.draw_text(f'{self.task}', 30, WHITE, WIDTH / 2, 50, self.font, False)

            # determine which button has the answer on it by coordinates in self.variations
            if self.place == self.variations[0]:
                self.answer = self.answer_button1
                self.incorrect1 = self.answer_button2
                self.incorrect2 = self.answer_button3
                self.variations.remove(self.place)
            elif self.place == self.variations[1]:
                self.answer = self.answer_button2
                self.incorrect1 = self.answer_button1
                self.incorrect2 = self.answer_button3
                self.variations.remove(self.place)
            elif self.place == self.variations[2]:
                self.answer = self.answer_button3
                self.incorrect1 = self.answer_button1
                self.incorrect2 = self.answer_button2
                self.variations.remove(self.place)
            self.bad_list = [self.incorrect1, self.incorrect2]

            if self.incorrect1.clicked or self.incorrect2.clicked:
                # help us with readability
                if isinstance(self.wrong, list):
                    wrong = ' '.join(self.wrong)
                    wrong2 = ' '.join(self.wrong2)
                else:
                    wrong = self.wrong
                    wrong2 = self.wrong2
                # draw red rect to indicate this is wrong answer
                if self.incorrect1.clicked:
                    pg.draw.rect(self.screen, '#8d021f', self.incorrect1.rect)
                    self.draw_text(f'{wrong}', 24, BLACK, self.variations[0], HEIGHT - 420, self.font, False)
                    pg.display.flip()
                elif self.incorrect2.clicked:
                    pg.draw.rect(self.screen, '#8d021f', self.incorrect2.rect)
                    self.draw_text(f'{wrong2}', 24, BLACK, self.variations[1], HEIGHT - 420, self.font, False)
                    pg.display.flip()
                self.mistakes += 1
                for _ in range(4):
                    # draw gold hollow rect around the correct button
                    pg.draw.rect(self.screen, '#f88917', pg.Rect(self.answer.x - (self.answer.width / 2) - 10,
                                                                 self.answer.y - (self.answer.height / 2) - 10,
                                                                 self.answer.width + 20, self.answer.height + 20), 5)
                    pg.display.flip()
                    time.sleep(0.2)
                    # make it blink by drawing a black one on it
                    pg.draw.rect(self.screen, BLACK, pg.Rect(self.answer.x - (self.answer.width / 2) - 10,
                                                             self.answer.y - (self.answer.height / 2) - 10,
                                                             self.answer.width + 20, self.answer.height + 20), 5)
                    pg.display.flip()
                    time.sleep(0.2)
                time.sleep(0.2)
                pg.draw.rect(self.screen, BLACK, pg.Rect(self.answer.x - (self.answer.width / 2) - 10,
                                                             self.answer.y - (self.answer.height / 2) - 10,
                                                             self.answer.width + 20, self.answer.height + 20), 5)
                time.sleep(0.1)
                # erase current task
                self.screen.fill(BLACK, (0, 0, 600, 100))
                # self.screen.fill(WHITE, (0, 100, 240, 40))
                self.task = random.choice(self.take_data)
                self.solution = self.INDEXES_ANSWERS[self.task]
                self.incorrect1.is_red = False

                # pick two random wrong solutions
                self.possible_set.remove(self.solution)
                self.wrong = random.sample(self.possible_set, 1)[0]
                self.possible_set.remove(self.wrong)
                self.wrong2 = random.sample(self.possible_set, 1)[0]
                if self.repeatable:
                    self.possible_set = list(set(self.INDEXES_ANSWERS.values()))
                else:
                    self.possible_set = list(self.INDEXES_ANSWERS.values())

                self.place = random.choice(self.variations)

            if self.answer.clicked:
                # hooray
                self.points += 1
                time.sleep(0.1)
                self.screen.fill(BLACK, (0, 0, 600, 100))
                self.task = random.choice(self.take_data)
                self.solution = self.INDEXES_ANSWERS[self.task]

                self.possible_set.remove(self.solution)
                self.wrong = random.sample(self.possible_set, 1)[0]
                self.possible_set.remove(self.wrong)
                self.wrong2 = random.sample(self.possible_set, 1)[0]
                if self.repeatable:
                    self.possible_set = list(set(self.INDEXES_ANSWERS.values()))
                self.possible_set = list(self.INDEXES_ANSWERS.values())

                self.place = random.choice(self.variations)

    def draw(self):
        # draw all sprites onto the screen, also text
        self.all_sprites.draw(self.screen)
        self.draw_text('LEAVE FOREVER', 20, WHITE, WIDTH/2, HEIGHT-65, self.font, False)

        self.draw_text(f'POINTS: {self.points}', 30, GREEN, 0, 0, self.font, True)
        self.draw_text(f'FAILURES: {self.mistakes}', 30, RED, WIDTH-130, 0, self.font, False)

        self.draw_text('RESTART', 20, WHITE, self.restart_button.x, self.restart_button.y-15, self.font, False)

        # draw all answers on the right buttons
        if isinstance(self.wrong, list):
            solution = ' '.join(self.solution)
            wrong = ' '.join(self.wrong)
            wrong2 = ' '.join(self.wrong2)
        else:
            solution = self.solution
            wrong = self.wrong
            wrong2 = self.wrong2
        self.draw_text(f'{solution}', 24, BLACK, self.place, HEIGHT - 420, self.font, False)
        self.draw_text(f'{wrong}', 24, BLACK, self.variations[0], HEIGHT - 420, self.font, False)
        self.draw_text(f'{wrong2}', 24, BLACK, self.variations[1], HEIGHT - 420, self.font, False)

        # set the variations again
        self.variations = [self.answer_button1.rect.centerx,
                           self.answer_button2.rect.centerx,
                           self.answer_button3.rect.centerx]

        pg.display.flip()

    def draw_text(self, text, size, color, x, y, font, alignment):
        # make a font
        font = pg.font.Font(font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (int(x), int(y))
        if alignment:
            text_rect.left = 1
        # draw it onto the screen
        self.screen.blit(text_surface, text_rect)

    def events(self):
        pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or pressed[pg.K_ESCAPE]:
                self.playing = False
                self.running = False

        if self.exit_button.rect.collidepoint(self.pos):
            if pg.mouse.get_pressed()[0]:
                self.playing = False
                self.running = False

        if self.restart_button.rect.collidepoint(self.pos):
            if pg.mouse.get_pressed()[0]:
                self.playing = False
                self.screen.fill(BLACK)
                self.new()

    def show_start_screen(self):
        # screen at the beginning
        self.screen.fill(BLACK)
        self.draw_text('CHOOSE YOUR GAME MODE', 38, '#FFD700', WIDTH/2, 45, self.font, False)
        pg.display.flip()
        self.waiting()

    def waiting(self):
        self.mode = ''
        waiting = True
        # make new temporary sprites
        temporary_sprites = pg.sprite.Group()
        capitals_mode = Button(WIDTH / 2, HEIGHT - 400, 400, 100, self, '#003d80')
        trigonometry_mode = Button(WIDTH / 2, HEIGHT - 200, 400, 100, self, '#003d80')
        temporary_sprites.add(capitals_mode)
        temporary_sprites.add(trigonometry_mode)
        temporary_sprites.draw(self.screen)
        pg.display.flip()
        while waiting:
            self.clock.tick(FPS)
            # update sprites and make mouse work
            temporary_sprites.draw(self.screen)
            self.pos = pg.mouse.get_pos()
            temporary_sprites.update()
            self.draw_text("COUNTRIES' CAPITALS", 24, WHITE, WIDTH / 2, HEIGHT - 420, self.font, False)
            self.draw_text("TRIGONOMETRY", 24, WHITE, WIDTH / 2, HEIGHT - 220, self.font, False)
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                # stop waiting and load geography
                if capitals_mode.clicked:
                    self.screen.fill(BLACK)
                    for sprite in temporary_sprites:
                        sprite.kill()
                    self.mode = 'geography'
                    waiting = False
                # stop waiting and load maths
                if trigonometry_mode.clicked:
                    self.screen.fill(BLACK)
                    for sprite in temporary_sprites:
                        sprite.kill()
                    self.mode = 'trigonometry'
                    waiting = False


g = Game()
g.show_start_screen()
while g.running:
    g.new()

pg.quit()
