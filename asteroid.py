import pygame, random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ang = (random.uniform(20, 50))
        new_vector_1 = self.velocity.rotate(ang)
        new_vector_2 = self.velocity.rotate(-ang)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = new_vector_1 * 1.2
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2.velocity = new_vector_2 * 1.2