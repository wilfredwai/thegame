import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    loop = 1
    while loop > 0:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    fill(black, rect=None, special_flags=0)
    pygame.display.flip()

if __name__ == "__main__":
    main()
