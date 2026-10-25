import pygame
from pygame.time import Clock

import circleshape
import player
import asteroid
import asteroidfield
from constants import LINE_WIDTH, PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    # intro
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    # basic settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    # groups and units
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (drawable,updatable)
    ship = player.Player(x, y)
    asteroid.Asteroid.containers = (asteroids, drawable,updatable)
    asteroidfield.AsteroidField.containers = (updatable)
    the_field = asteroidfield.AsteroidField()

    # the main loop
    i=0
    while i == 0:
        # event handling
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # frame rate
        screen.fill("black")
        dt = clock.tick(60) / 1000
        # update loop
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        # screen refres
        pygame.display.flip()






if __name__ == "__main__":
    main()
