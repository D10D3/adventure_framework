#this is not a part of the program, or even actual code
#it is just an outline to look at the whole program at a glance
#saved as a .py so it'll highlight and read nicely in my editor

_______________________ENGINE.PY________________________
imports and clear

class engine():
	def play():
		location = game_data.testroom1() 		#set starting location
		room_reader = game_data.room_reader()	#describe location (shortcut)
		reader = word_parser.reader() 			#parser class (shortcut)
		
		while True: 	#game loop
			room_reader.describe_room(location)	#describe location
			action = raw_input("Command?> ") 		#get user input
			action = reader.break_words(action) 	#break input into word list
			#now run the input list against parsers
			profanity = reader.profanity(action) 		#swearing?
			location = reader.exit(action,location) 	#moving to another room?
			look_at = reader.look_at(action,location) #looking at an object?
			recognized = reader.recognized(action) 	#returns error message if no known words
			system = reader.system(action) 			#system command?
			if system: #if reader.system receives "restart" it sets system to True
				restart = engine() #creates new engine instance
				restart.play() #starts new game loop
				
instantiate engine
start game loop

_____________________WORD_PARSER.PY_____________________

class reader(): 	#parser methods
	def break_words(action): 	#breaks 'action' input into a list of words
	def exit(action,location): 	#checks input to see if it's a move order
	def profanity(action): 		#checks for profanity
	def system(action): 			#checks for system commands
	def look_at(action,location): #checks for description query
	def recognized(action): 		#is known word? error message if not

______________________GAME_DATA.PY______________________

class room_reader(object):
	def describe_room(location): 	#prints room description
class default_room(object): 		#parent for room classes
#		***	Begin Room Classes		***
class testroom1(default_room):
class testroom2(default_room):
class testroom3(default_room):
#		***	Begin Word Lists		***
class words(object):
	system_commands = [list]			#load, save, restart, ect...
	inventory_commands = [list]		#get, drop equip, ect...
	nav_commands = [list]				#north, south, ect...
	verbs = [list]						#open, close, attack, move, ect...
	describers = [list]				#look, examine, ect...
	profanity = [list]					#shit, damn, fuck, ect...
	current_place_words = [list]	#here, room, place, ect...
	wordlists = [list of list]		#list of all word lists
	
