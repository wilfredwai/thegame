import pygame, sys
import asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import shot
def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable)

    dt = 0

    loop = 1
    while loop > 0:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        for draws in drawable: #draw step
            draws.draw(screen)
        pygame.display.flip()
        updatable.update(dt) #update step
        for run in asteroids:
            if run.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for ast_shot in asteroids:
            for each_shot in shots:
                if each_shot.collides_with(ast_shot):
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(ast_shot)
                    pygame.sprite.Sprite.kill(each_shot)

        AsteroidField()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
