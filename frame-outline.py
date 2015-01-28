#this is not a part of the program, or even actual code
#it is just an outline to look at the whole program at a glance
#saved as a .py so it'll highlight and read nicely in my editor

_______________________GAME.PY________________________
import os
os.system('cls')
import random
import game_engine
import game_data

class game_loop(object): #Game loop
	def play(object):
		location = game_data.testroom1() #starting location
		engine = game_engine.engine() #engine classes
		reader = game_engine.reader() #parser classes
		system = game_data.system.settings #engine data
		while True: 	#game loop
			engine.describe_room(location,system)			
			#get user input, then break it down into a list of words
			action = raw_input("Command?> ")
			action = reader.break_words(action)
			#now run the input list against a number of word checkers in the parser
			profanity = reader.profanity(action) 			#swearing?
			location = reader.exit(action,location,system) 	#moving to another room?
			look_at = reader.look_at(action,location,system) #looking at an object?
			recognized = reader.recognized(action) 			#returns error message if all words unknown
			system = reader.system(action,system) 			#system command?
			if system: #if reader.system receives "restart" it sets system to True
				restart = game_loop() #creates new game_loop instance
				restart.play() #starts new game loop

start = game_loop() #instantiate game_loop
start.play() #start game loop

_____________________GAME_ENGINE.PY_____________________
import game_data
class engine():
	def describe_room(location,system): #print description from room data
class reader(): 	#parser methods
	def break_words(action): 		#breaks 'action' input into a list of words
	def exit(action,location,system): 	#checks input to see if it's a move order
	def profanity(action): 			#checks for profanity
	def system(action,system): 		#checks for system commands
	def look_at(action,location,system): #checks for description query
	def recognized(action): 		#is known word? error message if not

______________________GAME_DATA.PY______________________
#		***	Game States		***
class system():
	brief = True #True = brief description, False = Verbose
	rooms_visited = [] 
	settings = [brief,rooms_visited]
#		***	Room Classes		***
class default_room(object): 		#parent for room classes
class testroom1(default_room):
class testroom2(default_room):
class testroom3(default_room):

#		***	Word Lists		***
class words(object):
	system_commands = [list]			#load, save, restart, ect...
	inventory_commands = [list]		#get, drop equip, ect...
	nav_commands = [list]				#north, south, ect...
	verbs = [list]						#open, close, attack, move, ect...
	describers = [list]				#look, examine, ect...
	profanity = [list]					#shit, damn, fuck, ect...
	current_place_words = [list]	#here, room, place, ect...
	wordlists = [list of list]		#list of all word lists
	
