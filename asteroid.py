import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20, 50)
        vector_01 = self.velocity.rotate(rand_angle)
        vector_02 = self.velocity.rotate(-rand_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_01 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_02 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_01.velocity = vector_01 * 1.2
        asteroid_02.velocity = vector_02 * 1.2
