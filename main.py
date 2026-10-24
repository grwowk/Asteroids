import pygame
from pygame.time import Clock

import circleshape
import player
from constants import LINE_WIDTH, PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    ship = player.Player(x, y)

    i=0
    while i == 0:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        ship.update(dt)
        ship.draw(screen)
        pygame.display.flip()






if __name__ == "__main__":
    main()
