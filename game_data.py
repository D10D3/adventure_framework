

#		***	Game States		***
class system():
	brief = True #True = brief description, False = Verbose
	
	rooms_visited = [] 
	
	settings = [brief,rooms_visited]


#		***	Room Classes		***
		
class default_room(object): #parent for room classes, fills in missing info with place holders
	data = {
		"title" : "Undefined Room",
		"short_description" : "A white empty room",
		}
	long_description = [
		"This is a white nondescript space awaiting data to describe it, ",
		"Like the 'Construct' in The Matrix"
		]
	inventory = {
		"nothing":"there is nothing there"
		}
	inventory_placed = {
		"nothing":" ",
		}
	objects = {
		"Nothing":"there isn't anything here"
		}	
		
class testroom1(default_room):
	data = {
		"title" : "Study",
		"short_description" : "A small study",
		}
	long_description = [
		"This is a small but cozy study with book shelves,",
		"a wingback chair and a phonograph"
		]
	inventory = {
		"record":"This is a resin platter record in a sleeve labeled 'Blue Danube'",
		"Emma":"This fat grey tabby cat has a tag that reads 'Emma'"
		}
	inventory_placed = {
		"record":"There is a record by the phonograph",
		"Emma":"There is a cat curled up on the chair named Emma"
		}
	objects = {
		"chair":"This is a large wingback style chair upholstered in red velvet.",
		"phonograph":"This is a cabinet style phonograph with a large hand-crank"
		}
	exits = ['north','east']

	def transition(self,exit):
		self.exit = exit
		if exit == 'north':
			location = testroom2()
		else:
			location = testroom3()
		return location
		
class testroom2(default_room):
	data = {
		"title" : "testroom2",
		"short_description" : "This is testroom2, It's a little dirty",
		}
	inventory = {
		"guitar":"a 1968 Harmoy Rocket hollow body guitar",
		"Tidbit":"a black and white cat who loves cheese"
		}
	objects = {
		"car":"A 1985 Buick Grand National",
		"futon":"A cheap futon from ikea"
		}
	exits = ['south','east']
	
	def transition(self,exit):
		self.exit = exit
		if exit == 'south':
			location = testroom1()
		else:
			location = testroom3()
		return location
		
class testroom3(default_room):
	data = {
		"title" : "testroom3",
		"short_description" : "This is testroom3, it smells like lemons",
		}
	inventory = {
		"pledge":"can of a lemony all all purpose surface cleaner",
		"Noosa":"a fluffy white cat"
		}
	objects = {
		"piano":"a black baby grand piano",
		"tardis":"a blue policebox, it may travel in time and space"
		}
	exits = ['north','south']

	def transition(self,exit):
		self.exit = exit
		if exit == 'north':
			location = testroom2()
		else:
			location = testroom1()
		return location

#		***	Word Lists		***

class words(object):
		
	system_commands = [
		"load",
		"save",
		"quit",
		"exit",
		"restart",
		"help",
		"?",
		"verbose",
		"brief",
		"score",
		"inv?",
		"q"
		]
		
	inventory_commands = [
		"inventory",
		"i",
		"get",
		"take",
		"equip",
		"put on",
		"wear",
		"drop",
		"throw"
		]

	nav_commands = [
		"north",
		"south",
		"east",
		"west",
		"northeast",
		"northwest",
		"southeast",
		"southwest",
		"n",
		"e",
		"s",
		"w",
		"ne",
		"nw",
		"se",
		"sw",
		"fore",
		"aft",
		"starboard",
		"port",
		"up",
		"down",
		"u",
		"d",
		"f",
		"a",
		"s",
		"p",
		"climb",
		"in",
		"out",
		"enter",
		"go"
		]
	
	verbs = [
		"g",
		"put",
		"turn",
		"turn on",
		"turn off",
		"move",
		"attack",
		"kill",
		"break",
		"eat",
		"drink",
		"shout",
		"read",
		"open",
		"close",
		"tie",
		"pray"
		]

	describers = [
		"look",
		"examine",
		"describe",
		"scan",
		"what"
		]
		
	profanity = [
		"fuck",
		"fucker",
		"motherfucker",
		"shit",
		"damn",
		"bitch",
		"crap",
		"piss",
		"dick",
		"darn",
		"cock",
		"pussy",
		"asshole",
		"fag",
		"bastard",
		"slut",
		"douche"
		]

	current_place_words = [
		"here",
		"room",
		"place",
		"location"
		]
		
	wordlists = [
		inventory_commands,
		system_commands,
		nav_commands,
		verbs,
		describers,
		profanity,
		current_place_words
		]
	