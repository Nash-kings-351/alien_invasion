import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	##screen = pygame.display.set_mode((self.screen_width, self.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	#make ship
	ship = Ship(ai_settings, screen)
	#make group of alien
	aliens = Group()
	# Make a group to store bullets in.
	bullets = Group()
	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Make the Play button.
	play_button = Button(ai_settings, screen, "Play")


	# Start the main loop for the game.
	while True:
		#checks  event from keyboard or mouse  i.e quit
		#gf.check_events(ship)
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		#updtes features of screen in this loop
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
		gf.update_screen(ai_settings, screen, stats,  sb, ship, aliens, bullets, play_button)

run_game()