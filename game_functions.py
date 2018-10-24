import sys
import pygame

def check_events(my_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

def update_screen(my_settings, screen):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(my_settings.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()