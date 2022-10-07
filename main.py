import pygame
import sys
from George import George
from directory_operator import get_background_image


class Game(object):

    def __init__(self):

        # Title
        pygame.display.set_caption('Przygody Georgea ')

        # Tick per second
        self.tps_max = 60.0

        # Load foto
        self.background = pygame.image.load(get_background_image())

        # Initialization
        pygame.init()

        WINDOW_WIDTH = 1920
        WINDOW_HEIGHT = 1030

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # Main Character
        self.player = George(self)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    print("menu")
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # Rendering
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):

        self.player.tick()

        # Character movements

    def draw(self):
        self.player.draw()


if __name__ == "__main__":
    Game()
