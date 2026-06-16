import pygame as pg
import Box
import Robot

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

        self.robot = Robot.Robot([100, 615])
        self.p_index = 0
        self.paths = [[100, 615],
                      [100, 570],
                      [120, 570],
                      [120, 105],
                      [120, 80],
                      [30, 80],
                      [30, 570],
                      [100, 570]]

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

        # Outbound
        pg.draw.rect(self.window, self.purple_dark, ( 50, 590, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (270, 590, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (490, 590, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (710, 590, 100, 50))
        pg.draw.rect(self.window, self.purple_dark, (930, 590, 100, 50))

        for i in range(5):
            if i % 2 == 0:
                # Inbound
                pg.draw.circle(self.window, self.green, (100 + (220 * i), 615), 7)
                pg.draw.circle(self.window, self.green, (100 + (220 * i), 570), 7)
                # Outbound
                pg.draw.circle(self.window, self.green, (100 + (220 * i), 35), 7)
                pg.draw.circle(self.window, self.green, (100 + (220 * i), 80), 7)
            else:
                # Inbound
                pg.draw.circle(self.window, self.green, (100 + (220 * i), 615), 7)
                # Outbound
                pg.draw.circle(self.window, self.green, (100 + (220 * i), 35), 7)

        # Corredor do meio
        for ii in range(26):
            # Corredor
            pg.draw.circle(self.window, self.red, (40 + (40 * ii), 325), 7)
            if ii in [7, 18]:
                # Outbound
                pg.draw.circle(self.window, self.green, (40 + (40 * ii), 570), 7)
                # Inbound
                pg.draw.circle(self.window, self.green, (40 + (40 * ii),  80), 7)
            else:
                # Outbound
                pg.draw.circle(self.window, self.red, (40 + (40 * ii), 570), 7)
                # Inbound
                pg.draw.circle(self.window, self.red, (40 + (40 * ii),  80), 7)

        # Paths
        #pg.draw.circle(self.window, self.red, (100, 615), 7)
        #pg.draw.circle(self.window, self.red, (100, 570), 7)
        #pg.draw.circle(self.window, self.red, (120, 570), 7)
        #pg.draw.circle(self.window, self.red, (120, 105), 7)
        #pg.draw.circle(self.window, self.red, (120, 80), 7)
        #pg.draw.circle(self.window, self.red, (30, 80), 7)
        #pg.draw.circle(self.window, self.red, (30, 570), 7)
        #pg.draw.circle(self.window, self.red, (100, 570), 7)
        # Path Outbound
        #pg.draw.circle(self.window, self.red, (100, 80), 7)
        #pg.draw.circle(self.window, self.red, (100, 35), 7)

    def creating_shelf_addresses(self):
        for column in range(25):
            for row in range(20):
                # Duas caixas por linha
                # Coordenada de parada do robo [[],[],[]]
                # Coordenada de posicionamento da caixa [[],[],[]]
                # pg.draw.rect(self.window, self.red, (50 + (c * 40), 100 + (l * 10), 10, 10))
                pass

    def robots_rend(self):
        if self.robot.next_pos == None:
            if self.p_index == 7:
                self.p_index = 0
            else:
                self.p_index += 1
            self.robot.next_pos = self.paths[self.p_index]
        self.robot.move()
        pg.draw.circle(self.window, self.blue, (self.robot.pos[0], self.robot.pos[1]), 7)


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
    rdc.robots_rend()


    rdc.last_click_status = mouse_input

    pg.display.update()
