import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, my_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.my_settings = my_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/shipr.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom

        # Or start each new ship at the left center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store decimal values for the ship's center.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += 1
        if self.moving_left and self.rect.left > 0:
            self.center_x -= 1
        if self.moving_up and self.rect.top > 0:
            self.center_y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += 1

        # Update rect object from self.center.
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)