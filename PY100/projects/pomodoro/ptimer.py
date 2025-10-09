# Features
# 25 minute pomodoro
# 5 minute break time

# Features to add
# A way to see how much time left

# A pomodoro timer that runs on the terminal
# Make sure to run a virtual environment before running file
"""
python3 -m venv venv
source venv/bin/activate
pip install pygame # might not be needed
"""
# You can use "deactivate"

import time
import pygame


def pomodoro():
	# Sets a variable to check for conditional
	start_timer = input("Start the 25 minute pomodoro? (Y / N) ")

	# Check if user wants to start timer
	while start_timer == "Y":
		
		start = True

		if start == True:
			# Load start sound file
			pygame.mixer.music.load("start.mp3")
			# Play start sound file
			pygame.mixer.music.play()

		# Timer
		time.sleep(1500)

		start = False

		if start == False:
			# Load end sound file
			pygame.mixer.music.load("end.mp3")
			# Play end sound file
			pygame.mixer.music.play()

		# 5 minute break
			short_break()

		# Loop continuation
		start_timer = input("Start the 25 minute pomodoro? (Y / N) ")

def short_break():
	# Sets a variable to check for conditional
	start_timer = input("Start the 5 minute break? (Y / N) ")

	# Check if user wants to start break
	if start_timer == "Y":
		
		start = True

		if start == True:
			# Load start sound file
			pygame.mixer.music.load("start.mp3")
			# Play start sound file
			pygame.mixer.music.play()

		# Timer
		time.sleep(300)

		start = False

		if start == False:
			# Load end sound file
			pygame.mixer.music.load("end.mp3")
			# Play end sound file
			pygame.mixer.music.play()

# Start timer
pygame.mixer.init()
pomodoro()