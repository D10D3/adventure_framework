import word_list
class reader(object):
	
	def break_words(self,action): #breaks 'action' input into a list of words
		words = action.split(' ')
		return words

	def exit(self,action,location): #checks input to see if it's a move order
		describers = word_list.words.describers
		exitcheck = 0
		looking_present = 0 #assume not looking
		for action_word in action:
			for i in describers:
				if action_word == i:
					looking_present += 1
				else:
					pass
		for action_word in action:
			for i in location.exits:
				if action_word == i:
					exitcheck += 1
				else:
					pass
			if not looking_present:
				if exitcheck:
					print ""
					print "You go %s" % action_word
					location = location.transition(action_word)
				else:
					pass
		return location
		
	def profanity(self,action): #checks for profanity
		profanity = word_list.words.profanity
		cursing = 0
		for action_word in action:
			for i in profanity:
				if action_word == i:
					cursing += 1
				else:
					pass
		if cursing:
			print "Such language!"
		else:
			pass
			
	def look_at(self,action,location): #checks for description query
		#first we get a list of describer words, and all of the location nouns
		describers = word_list.words.describers
		inventory = location.inventory.keys()
		objects = location.objects.keys()
		exits = location.exits
		#now we make a master noun list
		nouns = inventory + objects + exits
		
		looking_present = 0 #assume not looking
		noun_present = 0 #assume no noun
		look_word = "" #holder for a query word
		thing = ""  #holder for a noun
		for action_word in action:
			for i in describers:
				if action_word == i:
					look_word = i
					looking_present += 1
				else:
					pass
		
		for action_word in action:
			for noun in nouns:
				if action_word == noun:
					thing = action_word
					noun_present += 1
				else:
					pass
		
		if looking_present:
			if noun_present:
				if thing in inventory:
					print location.inventory[thing]
				elif thing in objects:
					print location.objects[thing]
				else:
					print "You will need to go %s to find out what is there" % thing
			if not noun_present:
				print "%s what?" % look_word
		else:
			pass
				
	def recognized(self,action): #checks input against all word lists, returns error message if unknown
		word_lists = word_list.words.wordlists
		known_word = 0
		
		for list in word_lists:
			for word in list:
				for action_word in action:
					if action_word == word:
						known_word += 1
					else:
						pass
		
		if not known_word:
			print "I don't understand that."
		else:
			pass
		