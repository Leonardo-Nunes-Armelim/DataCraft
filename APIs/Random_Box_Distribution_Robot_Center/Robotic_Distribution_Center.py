import Box
import Robot
import random
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

        self.robots_number = 20
        self.boxes_number = 50

        self.robots = [Robot.Robot([(random.randint(0, 119) * 10) + 5, (random.randint(0,  69) * 10) + 5]) for _ in range(self.robots_number)]
        
        self.boxes = [Box.Box('A', 'green', id + 1, [(random.randint(0, 119) * 10) + 5, (random.randint(0,  69) * 10) + 5]) for id in range(self.boxes_number)]

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

    def create_robot_path(self, robot):
        random_box = random.randint(0, self.boxes_number - 1)
        box_x = self.boxes[random_box].pos[0]
        box_y = self.boxes[random_box].pos[1]
        if abs(box_x - robot.pos[0]) > abs(box_y - robot.pos[1]):
            robot.paths = [[robot.pos[0], box_y], [box_x, box_y]]
        else:
            robot.paths = [[box_x, robot.pos[1]], [box_x, box_y]]

    def render(self):
        # Robots
        for robot in self.robots:
            if robot.next_pos == None:
                if len(robot.paths) == 0:
                    self.create_robot_path(robot)
                robot.next_pos = robot.paths[0]
            robot.move()
            if robot.next_pos is None and len(robot.paths) > 0:
                robot.paths.pop(0)
                if len(robot.paths) > 0:
                    robot.next_pos = robot.paths[0]
            pg.draw.circle(self.window, self.blue, (robot.pos[0], robot.pos[1]), 7)
        # Boxes
        for box in self.boxes:
            pg.draw.rect(self.window, self.green, (box.pos[0]-5, box.pos[1]-5, 10, 10))


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
    rdc.render()


    rdc.last_click_status = mouse_input

    pg.display.update()