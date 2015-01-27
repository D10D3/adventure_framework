import os
os.system('cls')
import random
import game_engine
import game_data

class game_loop(object): #Game loop
	#def __init__(self):
	def play(object):
		location = game_data.testroom1() #starting location
		engine = game_engine.engine()
		reader = game_engine.reader() #shortcut to parser
		system = game_data.system.settings
		while True:
			print""
			engine.describe_room(location,system)			
			print ""
			#get user input, then break it down into a list of words
			action = raw_input("Command?> ")
			action = reader.break_words(action)
			print""
			#now run the input list against a number of word checkers in the parser
			profanity = reader.profanity(action) #swearing?
			location = reader.exit(action,location,system) #moving to another room?
			look_at = reader.look_at(action,location,system) #looking at an object?
			recognized = reader.recognized(action) #returns error message if all words unknown
			system = reader.system(action,system) #system command?
			if system: #if reader.system receives "restart" it sets system to True
				restart = game_loop() #creates new game_loop instance
				restart.play() #starts new game loop
				
			
			
			
			

start = game_loop() #instantiate game_loop
start.play() #start game loop
