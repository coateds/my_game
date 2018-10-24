import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, my_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, my_settings.bullet_width, 
            my_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.color = my_settings.bullet_color
        self.speed_factor = 3

    def update(self):
        """Move the bullet on the screen."""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)