import os
import pygame as pg


class Flow_Forge:
    def __init__(self):
        self.white        = (255, 255, 255)
        self.black        = (  0,   0,   0)
        self.purple_dark  = (181, 181, 255)
        self.purple_light = (230, 230, 255)
        self.green        = (  0, 255,   0)
        self.green_light  = (180, 255, 180)
        self.blue         = (  0,   0, 255)

        self.window = pg.display.set_mode((1280, 720), pg.RESIZABLE)
        #self.window = pg.display.set_mode((0, 0), pg.FULLSCREEN)

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

    def botao(self, mouse):
        if mouse[0][0] >= 50 and mouse[0][0] <= 150 and mouse[0][1] >= 50 and mouse[0][1] <= 100:
            pg.draw.rect(self.window, self.purple_light, (50, 50, 100, 50))
            if mouse[2][0]:
                print('full screen')
                self.window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
            elif mouse[2][2]:
                print('resizable')
                self.window = pg.display.set_mode((1280, 720), pg.RESIZABLE)
        else:
            pg.draw.rect(self.window, self.purple_dark, (50, 50, 100, 50))
        pg.draw.rect(self.window, self.black, (50, 50, 100, 50), 3)

    def mouse_has_clicked(self, input):
            if self.last_click_status == input:
                return (False, False, False)
            else:
                left_button = False
                center_button = False
                right_button = False
                if self.last_click_status[0] == False and input[0] == True:
                    left_button = True
                if self.last_click_status[1] == False and input[1] == True:
                    center_button = True
                if self.last_click_status[2] == False and input[2] == True:
                    right_button = True

                return (left_button, center_button, right_button)

    def clear_window(self):
        pg.draw.rect(self.window, self.white, (0, 0, self.window.get_width(), self.window.get_height()))


flow_forge = FlowForge()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    # Mouse info
    mouse_position  = pg.mouse.get_pos()
    mouse_input = pg.mouse.get_pressed()
    mouse_click = flow_forge.mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)
    #print(mouse)

    # Game
    flow_forge.clock.tick(60)
    flow_forge.clear_window()
    flow_forge.botao(mouse)


    flow_forge.last_click_status = mouse_input

    pg.display.update()
