import pygame as pg


class Robotic_Distribution_Center:
    def __init__(self):
        self.black        = (  0,   0,   0)
        self.white        = (255, 255, 255)
        self.red          = (255,   0,   0)
        self.green        = (  0, 255,   0)
        self.green_light  = (180, 255, 180)
        self.blue         = (  0,   0, 255)
        self.purple_dark  = (181, 181, 255)
        self.purple_light = (230, 230, 255)

        self.window = pg.display.set_mode((1200, 700))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.clock = pg.time.Clock()

        # Mouse variables
        self.last_click_status = (False, False, False)

        self.robots = [[10, 10], [10, 30]]

    def map(self):

        # Robots
        for robot in self.robots:
            pg.draw.circle(self.window, self.blue, (robot[0], robot[1]), 7)

        # Boxes
        pg.draw.rect(self.window, self.green, (100, 100, 10, 10))

        # Shelves
        for c in range(25):
            pg.draw.line(self.window, self.black, (60 + (c * 40), 100), (60 + (c * 40), 300), 1)
            for l in range(21):
                pg.draw.line(self.window, self.black, (50 + (c * 40), 100 + (l * 10)), (70 + (c * 40), 100 + (l * 10)), 1)
        for c in range(25):
            pg.draw.line(self.window, self.black, (60 + (c * 40), 350), (60 + (c * 40), 550), 1)
            for l in range(21):
                pg.draw.line(self.window, self.black, (50 + (c * 40), 350 + (l * 10)), (70 + (c * 40), 350 + (l * 10)), 1)

        # Warehouse
        pg.draw.rect(self.window, self.black, (10, 10, 1060, 630), 1)

        # Inbound
        pg.draw.rect(self.window, self.purple_dark, ( 50, 10, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (270, 10, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (490, 10, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (710, 10, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (930, 10, 100, 50))
        #pg.draw.rect(self.window, self.purple_dark, (  10, 60, 40, 40))
        #pg.draw.rect(self.window, self.purple_dark, (1030, 60, 40, 40))

        # Outbound
        pg.draw.rect(self.window, self.purple_dark, ( 50, 590, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (270, 590, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (490, 590, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (710, 590, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (930, 590, 100, 50))
        #pg.draw.rect(self.window, self.purple_dark, (  10, 550, 40, 40))
        #pg.draw.rect(self.window, self.purple_dark, (1030, 550, 40, 40))

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


rdc = Robotic_Distribution_Center()


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
    mouse_click = rdc.mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)
    #print(mouse)

    # Game
    rdc.clock.tick(60)
    rdc.clear_window()
    rdc.map()


    rdc.last_click_status = mouse_input

    pg.display.update()
