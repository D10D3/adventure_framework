import os
os.system('cls')
import random
import word_parser
import game_data

class engine(object): #Game loop
	#def __init__(self):
	def play(object):
		location = game_data.testroom1() #starting location
		room_reader = game_data.room_reader()
		reader = word_parser.reader() #shortcut to parser
		while True:
			print""
			room_reader.describe_room(location)			
			print ""
			#get user input, then break it down into a list of words
			action = raw_input("Command?> ")
			action = reader.break_words(action)
			print""
			#now run the input list against a number of word checkers in the parser
			profanity = reader.profanity(action) #swearing?
			location = reader.exit(action,location) #moving to another room?
			look_at = reader.look_at(action,location) #looking at an object?
			recognized = reader.recognized(action) #returns error message if all words unknown
			system = reader.system(action) #system command?
			if system: #if reader.system receives "restart" it sets system to True
				restart = engine() #creates new engine instance
				restart.play() #starts new game loop
			
			
			

start = engine() #instantiate engine
start.play() #start game loop
