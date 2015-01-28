import game_data

class engine(object):

	def describe_room(self,location,system_data): #print description from room data
		print ""
		print location.title
		print location.short_description
		#if new room, or verbose, print long description
		if location.title not in system_data.rooms_visited:
			system_data.rooms_visited.append(location.title)
			for i in location.long_description:
				print i
			print ""
		elif system_data.brief == False:
			for i in location.long_description:
				print i
			print ""
		#describe room inventory
		for item in location.inventory.keys():
			for placed in location.inventory_placed.keys():
				if item == placed:
					print location.inventory_placed[item]

		exits_list = "Exits: "
		for key in location.exits:
			exits_list += key
			exits_list += ", "
		print exits_list
		print ""

class parser(object): #Various parsers for acting on user input
	
	def break_words(self,action): #breaks 'action' input into a list of words
		words = action.split(' ')
		print"" #dumb, but helps formatting
		return words

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
		exitcheck = 0#these three are holders for checking input against lists
		navcheck = 0 #we start assuming they are not on the list
		looking_present = 0
		going_to = ""
		
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
			
	def system(self,action,system_data): #checks for system commands
		system_commands = game_data.words.system_commands
		is_system = 0 #assume action is not a system command
		system_action = "" #sets space for detected system command
		for action_word in action:
			for i in system_commands:
				if action_word == i:
					system_action = action_word
					is_system += 1

		if is_system:
			if action_word == "inv?":
				for inv_word in game_data.words.inventory_commands:
					print inv_word 
			elif action_word == "load":
				print "Command not yet implemented"
			elif action_word == "save":
				print "Command not yet implemented"
			elif action_word == "verbose":
				system_data.brief = False
				print "Setting Verbose, Always give full room description"
			elif action_word == "brief":
				system_data.brief = True
				print "Setting brief, Only give room full description on first visit"
			elif action_word == "score":
				print "Command not yet implemented"
			elif action_word == "restart":
				return True
			elif action_word == "quit":
				quit()
			elif action_word == "exit":
				quit()
			elif action_word == "q":
				quit()
			elif action_word == "?" or "help":
				print "Adventure Framework ver0.5 by D10d3"
				print ""
				print "System commands:"
				print "	inv? : Lists inventory commands the player can use"
				print "	load : Command not yet implemented"
				print "	save : Command not yet implemented"
				print "	verbose : Always give full room description"
				print "	brief : Only give room full description on first visit"
				print "	score : Command not yet implemented"
				print "	restart : Restarts the game"
				print "	help or ? : Displays this information"
				print "	exit or quit or q : Exits the game"
			
	def look_at(self,action,location,system_data): #checks for description query
		#first we get a list of describer words, and all of the location nouns
		describers = game_data.words.describers
		inventory = location.inventory.keys()
		objects = location.objects.keys()
		exits = location.exits.keys()
		current_place_words = game_data.words.current_place_words
		#now we make a master noun list
		nouns = inventory + objects + exits + current_place_words
		
		looking_present = 0 #assume not looking
		noun_present = 0 #assume no noun
		look_word = "" #holder for a query word
		thing = ""  #holder for a noun
		for action_word in action:
			for i in describers:
				if action_word == i:
					look_word = i
					looking_present += 1
		
		for action_word in action:
			for noun in nouns:
				if action_word == noun:
					thing = action_word
					noun_present += 1
		
		if looking_present:
			if noun_present:
				if thing in inventory:
					print location.inventory[thing]
				elif thing in objects:
					print location.objects[thing]
				elif thing in current_place_words:
					for line in location.long_description:
						print line
				else:
					print "You will need to go %s to find out what is there" % thing
			if not noun_present:
				print "%s?" % look_word
				
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
		
