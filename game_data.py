

#		***	Game States		***
class system():
	brief = True #True = brief description, False = Verbose
	
	rooms_visited = [] 
	
	settings = [brief,rooms_visited]
	class player():
		player_inventory = {}

#		***	Room Classes		***
class map():
		
	class default_room(object): #parent for room classes, fills in missing info with place holders
		title = "Undefined Room"
		short_description = "A white empty room"
		long_description = [
			"This is a white nondescript space awaiting data to describe it, ",
			"Like the 'Construct' in The Matrix"
			]
		inventory = {
			"nothing":"there is nothing there"
			}
		inventory_placed = {
			"nothing":"There are no visible objects",
			}
		objects = {
			"Nothing":"there isn't anything here"
			}
		exits = {
			'up' : "Study"
			}
			
	class Study(default_room):
		title = "Study"
		short_description = "A small Study"
		long_description = [
			"This is a small but cozy Study with book shelves,",
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
		exits = {
			'north' : "Parlor",
			'east' : "Ballroom"
			}
			
	class Parlor(default_room):
		title = "Parlor"
		short_description = "It is warm and inviting here"
		long_description = [
			"This is a parlor with polished hardwood floors, an",
			"oriental rug, and a sofa facing a fireplace."
			]
		inventory = {
			"guitar":"It's a 1968 Harmoy Rocket hollow body guitar",
			"Tidbit":"This is black and white cat who loves cheese"
			}
		inventory_placed = {
			"guitar":"A guitar leans against the sofa.",
			"Tidbit":"There is a cat named Tidbit asleep in front of the fire"
			}
		objects = {
			"Sofa":"It's a Victorian style sofa with grey and dark grey vertical stripes",
			"rug":"This oriental rug has excellent knot work and patterns",
			"fireplace":"The brick hearth fireplace has several logs burning in it"
			}
		exits = {
			'south' : "Study",
			'east' : "Ballroom"
			}
			
	class Ballroom(default_room):
		title = "Ballroom"
		short_description = "This is the Ballroom, it smells like lemons"
		long_description = [
			"This is a large ballroom with parquet flooring, crystal chandeliers",
			"and a vaulted ceiling. Sunlight streams in through a domed skylight." ,
			"There is A wooden blue box in one corner, about the size of a",
			"phonebooth. it has a sign on it that says 'Police Box'."]
		inventory = {
			"pledge":"It's can of a lemony all all purpose surface cleaner",
			"Noosa":"Noosa is a fluffy white cat with blue eyes."
			}
		inventory_placed = {
			"pledge":"There's a can of pledge sitting on the floor",
			"Noosa":"A white cat is sitting on the piano, her tag reads 'Noosa'."
			}
		objects = {
			"piano":"It is a black baby grand piano",
			"tardis":"It's a blue policebox, it may travel in time and space",
			"policebox":"It's a blue policebox, it may travel in time and space",
			"police":"It's a blue policebox, it may travel in time and space"
			}
		exits = {
			'north' : "Parlor",
			'south' : "Study"
			}
	
	room_list = {
		"Study":Study(),
		"Parlor":Parlor(),
		"Ballroom":Ballroom()
		}

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
	
	convert_direction = {
		"north":"n",
		"south":"s",
		"east":"e",
		"west":"w",
		"northeast":"ne",
		"southeast":"se",
		"northwest":"nw",
		"southwest":"sw",
		"up":"u",
		"down":"d"
		}
