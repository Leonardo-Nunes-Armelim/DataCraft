import math

class Robot:
    def __init__(self, pos):
        self.pos = [float(pos[0]), float(pos[1])]
        self.paths = []

        self.speed = 0.0
        self.max_speed = 1.0
        self.acceleration = 0.01

        self.next_pos = None

    def move(self):

        if self.next_pos is None:
            self.speed = 0
            return

        dx = self.next_pos[0] - self.pos[0]
        dy = self.next_pos[1] - self.pos[1]

        distance = math.sqrt(dx*dx + dy*dy)

        if distance < 0.5:
            self.pos[0] = self.next_pos[0]
            self.pos[1] = self.next_pos[1]
            self.speed = 0
            self.next_pos = None
            return

        # Distância necessária para frear
        braking_distance = (self.speed * self.speed) / (2 * self.acceleration)

        if distance <= braking_distance:
            # Freando
            self.speed -= self.acceleration
        else:
            # Acelerando
            self.speed += self.acceleration

        self.speed = max(0.1, min(self.speed, self.max_speed))

        # Evita ultrapassar o destino
        step = min(self.speed, distance)

        self.pos[0] += (dx / distance) * step
        self.pos[1] += (dy / distance) * step