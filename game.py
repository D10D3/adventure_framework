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
		last_input = "look here"
		while True:
			engine.describe_room(self.location,self.system,self.items)			
			#get user input, then break it down into a list of words
			input = raw_input("Command?> ")
			if input == "g":
				input = last_action
			last_action = input
			action = parser.break_words(input)
			nouns = []
			verb = ""
			event = ""
			#now run the input list against a number of word checkers in the parser
			recognized = parser.recognized(action) 				#returns error message if all words unknown
			if recognized == True:
				nouns = parser.get_nouns(action,self.location,self.items,self.player)#get nouns from input
				verb = parser.get_verb(action)
				profanity = parser.profanity(action) 	#swearing?
				look_at = parser.look_at(verb,nouns,self.location,self.items,self.player) 	#looking at an object?
				#begin events
				event = engine.event_handler(self.location,self.items,self.player,self.words,nouns,verb) #checks events
				if event == "get" or "drop":
					engine.inventory(event,self.location,self.items,self.player,nouns,verb)
				if event == "put" or "get from":
					engine.place_item(event,self.location,self.items,self.player,nouns,verb)
					
				self.location = parser.exit(action,self.location,self.system,self.map) 	#moving to another room?
				system = parser.system(self.system,verb)		#system command?
				if system: #if parser.system receives "restart" it sets system to True
					restart = game_loop() #creates new game_loop instance
					restart.play() #starts new game loop
			print""
			

start = game_loop() #instantiate game_loop
start.play() #start game loop

	

