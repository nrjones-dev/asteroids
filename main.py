import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_time = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore
    AsteroidField.containers = updatable  # type: ignore
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)  # type: ignore

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 fps
        dt = game_time.tick(60) / 1000


if __name__ == "__main__":
    main()
