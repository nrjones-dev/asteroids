import os
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from constants import *
from player import Player


def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "600,300"
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_time = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = updatable  # type: ignore
    Player.containers = (updatable, drawable)  # type: ignore
    Bullet.containers = (bullets, updatable, drawable)  # type: ignore

    asteroid_field = AsteroidField()

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for bullet in bullets:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 fps
        dt = game_time.tick(60) / 1000


if __name__ == "__main__":
    main()
