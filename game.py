import os
os.system('cls')
import random
import game_engine
import game_data


class game_loop(object): #Game loop
	def __init__(self):
		self.map = game_data.map() 			#rooms superclass
		self.system = game_data.system() 	#engine data
		self.location = self.map.Study() #starting location

	def play(self):
		#instanced methods
		engine = game_engine.engine() #engine classes
		parser = game_engine.parser() #parser classes
		
		while True:
			engine.describe_room(self.location,self.system)			
			#get user input, then break it down into a list of words
			action = raw_input("Command?> ")
			action = parser.break_words(action)
			#now run the input list against a number of word checkers in the parser
			profanity = parser.profanity(action) 					#swearing?
			self.location = parser.exit(action,self.location,self.system,self.map) 	#moving to another room?
			look_at = parser.look_at(action,self.location,self.system) 	#looking at an object?
			recognized = parser.recognized(action) 				#returns error message if all words unknown
			system = parser.system(action,self.system) 			#system command?
			if system: #if parser.system receives "restart" it sets system to True
				restart = game_loop() #creates new game_loop instance
				restart.play() #starts new game loop
				

start = game_loop() #instantiate game_loop
start.play() #start game loop

	

