from sys import _current_exceptions

import pygame
import random

import circleshape
import constants
from logger import log_event


class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw (self, screen: pygame.Surface):
        pygame.draw.circle (screen,"white", self.position , self.radius, constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        change = random.uniform(20,50)
        new1 = self.velocity.rotate(change)
        new2 = self.velocity.rotate(-change)
        size = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position[0],self.position[1],size)
        new_asteroid_2 = Asteroid(self.position[0],self.position[1],size)
        new_asteroid_1.velocity = new1
        new_asteroid_2.velocity = new2
        new_asteroid_1.velocity *= 1.2
        new_asteroid_2.velocity *= 1.2
        return new_asteroid_1, new_asteroid_2
