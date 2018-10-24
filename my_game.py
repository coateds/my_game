import pygame

import game_functions as gf

from settings import Settings

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode(
        (my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption("My Game")

    # Start the main loop for the game.
    while True:
        gf.check_events(my_settings, screen)

        gf.update_screen(my_settings, screen)

run_game()