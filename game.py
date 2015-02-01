import os
os.system('cls')
import random
import game_engine
import game_data


class game_loop(object): #Game loop
	def __init__(self):
		self.player = game_data.player() #player data
		self.items = game_data.items() #all Gear,Inventory, and static items
		self.map = game_data.map() 			#rooms superclass
		self.system = game_data.system() 	#engine data
		self.words = game_data.words()
		self.location = self.map.starting_room #starting location
		

	def play(self):
		#instanced methods
		engine = game_engine.engine() #engine classes
		parser = game_engine.parser() #parser classes
		
		while True:
			engine.describe_room(self.location,self.system,self.items)			
			#get user input, then break it down into a list of words
			action = raw_input("Command?> ")
			action = parser.break_words(action)
			nouns = []
			verb = ""
			#now run the input list against a number of word checkers in the parser
			recognized = parser.recognized(action) 				#returns error message if all words unknown
			if recognized == True:
				nouns = parser.get_nouns(action,self.location,self.items,self.player)#get nouns from input
				verb = parser.get_verb(action)
				engine.event_handler(action,self.location,self.items,self.player,self.words,nouns) #checks for and handles events
				profanity = parser.profanity(action) 					#swearing?
				self.location = parser.exit(action,self.location,self.system,self.map) 	#moving to another room?
				look_at = parser.look_at(verb,nouns,self.location,self.items,self.player) 	#looking at an object?
				system = parser.system(action,self.system) 			#system command?
				if system: #if parser.system receives "restart" it sets system to True
					restart = game_loop() #creates new game_loop instance
					restart.play() #starts new game loop
				

start = game_loop() #instantiate game_loop
start.play() #start game loop

	

