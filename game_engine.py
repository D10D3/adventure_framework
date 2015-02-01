import game_data
import os
class engine(object):

	def describe_room(self,location,system_data,items): #print description from room data
		print ""
		print location.title
		#if new room, or verbose, print long description
		if location.title not in system_data.rooms_visited:
			system_data.rooms_visited.append(location.title)
			for i in location.long_description:
				print i
			print ""
		elif system_data.brief == False:
			for i in location.long_description:
				print i
		else:
			print location.short_description
		#describe room inventory
		print "item descriptions:"
		for item in location.inventory:
			print item['placed']
		print ""

	#	*** BEGIN EVENT FUNCTIONS ***
	def event_handler(self,location,items,player,words,nouns,verb): #triggers events from player input
		#inventory router
		
		if verb in words.inventory_commands:
			if verb == "inventory":
				print "Inventory:"
				for item in player.inventory:
					print "	%s"%item['name']
			elif verb == "i":
				print "Inventory:"
				for item in player.inventory:
					print "	%s"%item['name']					
			elif verb == "get":
				return "get"	
			elif verb == "take":
				return "get"					
			elif verb == "drop":
				return "drop"

	def	move(): #change room
		pass
	def	inventory(self,action,location,items,player,nouns,verb): #add or remove player_inventory
		if action == "get":
			for noun in nouns:
				for item in location.inventory:
					if noun == item:
						location.inventory.remove(item)
						player.inventory.append(item)
						print "you get %s" % item['name']
		elif action == "drop":
			for noun in nouns:
				for item in player.inventory:
					if noun == item:
						location.inventory.append(item)
						player.inventory.remove(item)
						print "you drop %s" % item['name']
		
				
	def	place_item(): #placing item: "Put jewel in box"
		pass
	def	change_exit(): #add or remove an exit
		pass
	def	change_static(): #add or remove static objects
		pass
	def	room_inventory(): #add or remove room_inventory
		pass
	def	change_mob(): #add or remove mob
		pass
	def	change_room_desc(): #change room descriptions
		pass
	def	health(): #change player health
		pass
	def	combat(): #initiate combat
		pass
	def	talk(): #initiate conversation
		pass
class parser(object): #Various parsers for acting on user input
	
	def break_words(self,action): #breaks 'action' input into a list of words
		words = action.split(' ')
		print"" #dumb, but helps formatting
		return words
	def get_nouns(self,action,location,items,player): #pull nouns from player input
		#loc_inv = location.inventory
		#loc_static = location.static
		#player_inv = player.inventory
		exits = location.exits.keys()
		nouns = [] #holder for found nouns
		for word in action:
			for item in location.inventory:
				if item['name'] == word:
					nouns.append(item)
			for item in location.static:
				if item['name'] == word:
					nouns.append(item)
			for item in player.inventory:
				if item['name'] == word:
					nouns.append(item)
		return nouns
	def get_verb(self,action):
		current_place_words = game_data.words.current_place_words
		verb = ""
		words = game_data.words()
		verb_list = []
		verb_list.append(words.inventory_commands)
		verb_list.append(words.verbs)
		verb_list.append(words.describers)
		verb_list.append(words.nav_commands)
		verb_list.append(words.system_commands)
		for word in action:
			for list in verb_list:
				if word in list:
					verb = word
		for desc in words.describers:
			if verb == desc:
				for word in current_place_words:
					for action_word in action:
						if action_word == word:
							verb = "look here"
		return verb

	def exit(self,action,location,system_data,map_data): #checks input to see if it's a move order
		#we are checking for three things here:
		#we are checking for three things here:
		#	is the user input just trying to look at an exit?
		#	If not, is the input on the list of possible nav commands?
		#	if so, is it actually a valid exit for this location?
		#		detected look-direction inputs are ignored, 
		#		parser.look_at will also detect this and issue and error message
		#if all of those are satisfied and it's a good command, the location is changed
		describers = game_data.words.describers
		nav_commands = game_data.words.nav_commands
		converter = game_data.words.convert_direction
		exitcheck = 0#these three are holders for checking input against lists
		navcheck = 0 #we start assuming they are not on the list
		looking_present = 0
		going_to = ""
		
		#convert single letter directions.
		for dir in converter:
			conv = []
			conv.append(converter[dir])
			dirlist = []
			dirlist.append(dir)
			if action == conv:
				action = dirlist
		
		
		for action_word in action: #start processing user input
			for look in describers:#are you just trying to look at an exit?
				if action_word == look:
					looking_present += 1
				for nav in nav_commands: #does it contain a nav command?
					if action_word == nav:
						navcheck += 1
					for exit in location.exits: #is it on the list of exits for this location?
						exitkey = location.exits[exit]
						if action_word == exit:
							exitcheck += 1
							going_to = exitkey
							
		#having determined if input is just looking, is a nav command, and is on the exit list
		#we now start acting on that info
		if not looking_present:
			if navcheck:
				if not exitcheck:
					print "You can't go that way"
				else:
					print ""
					print "You go %s" % action_word
					for room in map_data.room_list:
						if room == going_to:
							location = map_data.room_list[going_to]
		return location
		
	def profanity(self,action): #checks for profanity
		profanity = game_data.words.profanity
		cursing = 0
		for action_word in action:
			for i in profanity:
				if action_word == i:
					cursing += 1
		if cursing:
			print "Such language!"
			
	def system(self,system_data,verb): #checks for system commands
		system_commands = game_data.words.system_commands
		for word in system_commands:
			if verb == word:
				if verb == "inv?":
					for inv_word in game_data.words.inventory_commands:
						print inv_word 
				elif verb == "load":
					print "Command not yet implemented"
				elif verb == "save":
					print "Command not yet implemented"
				elif verb == "verbose":
					system_data.brief = False
					print "Setting Verbose, Always give full room description"
				elif verb == "brief":
					system_data.brief = True
					print "Setting brief, Only give room full description on first visit"
				elif verb == "score":
					print "Command not yet implemented"
				elif verb == "restart":
					return True
				elif verb == "quit":
					quit()
				elif verb == "exit":
					quit()
				elif verb == "q":
					quit()
				elif verb == "clear":
					os.system('cls')
				elif verb == "?" or "help":
					print "Adventure Framework ver0.5 by D10d3"
					print "    -= An adventure engine =-"
					print ""
					print "In addition to the following system commands you may type any action"
					print "that comes to mind with varying degrees of success. When interacting"
					print "with objects try to always place the verb before the noun."
					print "Thanks for playing."
					print ""
					print "System commands:"
					print "	clear = Clear the screen"
					print "	inv? : Lists inventory commands the player can use"
					print "	load : Command not yet implemented"
					print "	save : Command not yet implemented"
					print "	verbose : Always give full room description"
					print "	brief : Only give room full description on first visit"
					print "	score : Command not yet implemented"
					print "	restart : Restarts the game"
					print "	help or ? : Displays this information"
					print "	exit or quit or q : Exits the game"
	
			
	def look_at(self,verb,nouns,location,items,player): #checks for description query
		#first we get a list of describer words, and all of the possible nouns
		describers = game_data.words.describers
		loc_inv = location.inventory
		loc_static = location.static
		player_inv = player.inventory
		exits = location.exits.keys()
		#current_place_words = game_data.words.current_place_words
		present = 0 #assumes you are looking at nothing that's there.
		if verb == "look here":
			present += 1
			for i in location.long_description:
				print i
		for word in describers:
			if verb == word:
				for noun in nouns:
					print noun['desc']
					present += 1
		for list in game_data.words.wordlists:
			if verb in list:
				present +=1
		
		if verb in exits:
			print "You will need to go %s to find out what is there" % verb
			present += 1
		if not present:
			print "What are you looking at?"
				
	def recognized(self,action): #is known word? error message if not
		game_datas = game_data.words.wordlists
		known_word = 0
		
		for list in game_datas:
			for word in list:
				for action_word in action:
					if action_word == word:
						known_word += 1
		
		if not known_word:
			print "I don't understand that."
		else:
			return True
		
