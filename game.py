import os
os.system('cls')
import random
import game_engine
import game_data

class game_loop(object): #Game loop
	def play(object):
		map = game_data.map() #rooms superclass
		engine = game_engine.engine() #engine classes
		parser = game_engine.parser() #parser classes
		system = game_data.system.settings #engine data
		location = map.testroom1() #starting location
		
		#two different routes to the same variable.
		#print location.title
		
		
		while True:
			print"" #put in room reader
			engine.describe_room(location,system)			
			print "" #put in room reader
			#get user input, then break it down into a list of words
			action = raw_input("Command?> ")
			action = parser.break_words(action)
			print""
			#now run the input list against a number of word checkers in the parser
			profanity = parser.profanity(action) 					#swearing?
			location = parser.exit(action,location,system,map) 	#moving to another room?
			look_at = parser.look_at(action,location,system) 	#looking at an object?
			recognized = parser.recognized(action) 				#returns error message if all words unknown
			system = parser.system(action,system) 				#system command?
			if system: #if parser.system receives "restart" it sets system to True
				restart = game_loop() #creates new game_loop instance
				restart.play() #starts new game loop
				
			
			
			
			

start = game_loop() #instantiate game_loop
start.play() #start game loop

