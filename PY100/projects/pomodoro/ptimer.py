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

# Start pygame mixer
pygame.mixer.init()


# Sets a variable to check for conditional
start_timer = input("Start the 25 minute timer? (Y / N) ")

# Check if user wants to start timer
while start_timer == "Y":
	
	start = True

	if start == True:
		# Load start sound file
		pygame.mixer.music.load("start.mp3")
		# Play start sound file
		pygame.mixer.music.play()

	# Timer
	time.sleep(10)

	start = False

	if start == False:
		# Load end sound file
		pygame.mixer.music.load("end.mp3")
		# Play end sound file
		pygame.mixer.music.play()

	
	# Loop continuation
	start_timer = input("Start the 25 minute timer? (Y / N) ")