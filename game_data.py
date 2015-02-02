

class items():
	
	#Gear items: anything that can be equipped
		# gear classes
		# gear size is the amount of space gear take up in player inventory when NOT equipped
		# equipped gear takes no bag space
		# all armor and damage values for equipped gear are tallied to determine player stats
		# Add a routine to the equipment swap function that will check is a gear slot of empty
		# if a slot is empty it will place the default gear there.
		
	default_head = {
		"name" : "bare-head",
		"desc" : "You aren't wearing anything on your head",
		"type" : "head",
		"damage" : 0,
		"armor" : 0,
		"size" : 0,
		"bag_space" : 0,
		"placed" : "Need to define placed for item"
		}
	default_hand = {
		"name" : "empty-hands",
		"desc" : "You don't have anything readied in your hands.",
		"type" : "hand",
		"damage" : 1, #fist
		"armor" : 0,
		"size" : 0,
		"bag_space" : 1, #held in off hand
		"placed" : "Need to define placed for item"
		}
	default_body = {
		"name" : "loin-cloth",
		"desc" : "While it lacks in protection it at least protects your modesty",
		"type" : "body",
		"damage" : 0,
		"armor" : 0,
		"size" : 0,
		"bag_space" : 0,
		"placed" : "Need to define placed for item"
		}
	default_bag = {
		"name" : "No-bag",
		"desc" : "No-bag",
		"type" : "bag",
		"damage" : 0,
		"armor" : 0,
		"size" : 0,
		"bag_space" : 0,
		"placed" : "Need to define placed for item"
		}
	default_special = {
		"name" : "quick-wit",
		"desc" : "Mom always said you were smart",
		"type": "special",
		"damage": 0,
		"armor": 0,
		"size": 0,
		"bag_space" : 0,
		"placed" : "Need to define placed for item"
		}
		
	wizard_hat = {
		"name" : "wizard-hat",
		"desc" : "This enchanted blue hat is embroidered with stars",
		"type": "head",
		"damage": 1, #+1 "damage"from enchantment
		"size" : 1,
		"placed" : "There's a wizard-hat here.",
		"container":False,
		}
	wand = {
		"name" : "wand",
		"desc" : "This wand is finely carved from a dark wood and inscribed with runes",
		"type" : "hand",
		"size" : 1,
		"damage": 4,
		"placed" : "Need to define placed for item",
		"container":False,
		}
	robes = {
		"name" : "robes",
		"desc" : "While somewhat travel worn, these blue robes are quite comfy.",
		"type": "body",
		"size": 1,
		"armor": 1,
		"placed" : "Need to define placed for item"
		}
	satchel = {
		"name" : "satchel",
		"desc" : "This is a brown leather satchel with a shoulder strap.",
		"type": "bag",
		"size": 2,
		"bag_space" : 6, 
		"inventory":[],
		"placed" : "Need to define placed for item",
		"container":True,
		}
	ring_protection = {
			"name" : "ring-protection",
			"desc" : "An old wizard gave you this ring, it's enchantment helps deflect blows",
			"type": "special",
			"damage": 0,
			"armor": 1,
			"size": 0, #small objects don't effect bag space
			"placed" : "Need to define placed for item",
			"container":False,
			}
	#Inventory Items:	: anything that can be carried
	# item = {
		# "name":"",
		# "desc":"",
		# "placed":"",
		# "event":""
		# }
	record = {
		"name":"record",
		"desc":"This is a resin platter record in a sleeve labeled 'Blue Danube'",
		"placed":"There is a record here",
		"event":None,
		"container":False,
		}
	Emma = {
		"name":"Emma",
		"desc":"This fat grey tabby cat has a tag that reads 'Emma'",
		"placed":"There is a cat curled up here named Emma",
		"event":None,
		"container":False,
		}
	Tidbit= {
		"name":"Tidbit",
		"desc":"This is black and white cat who loves cheese",
		"placed":"There is a cat named Tidbit here.",
		"event":None,
		"container":False,
		}
	guitar = {
		"name":"guitar",
		"desc":"It's a 1968 Harmoy Rocket hollow body guitar",
		"placed":"A guitar leans against the sofa.",
		"event":None,
		"container":False,
		}
	pledge = {
		"name":"pledge",
		"desc":"It's can of a lemony all all purpose surface cleaner",
		"placed":"There's a can of pledge sitting on the floor",
		"event":None,
		"container":False,
		}
	Noosa = {
			"name":"Noosa",
			"desc":"Noosa is a fluffy white cat with blue eyes.",
			"placed":"A white cat is sitting here, her tag reads 'Noosa'.",
			"event":None,
			"container":False,
			}
	crate = {
		"name":"crate",
		"desc":"This is a small wooden open topped crate.",
		"placed":"there is a crate here",
		"event":None,
		"container":True,
		"inventory":[],
		"space":1,
		}
		
			
#STATIC Items: things that can't move but can be interacted with
		#the eventual layout of static objects will be determined by the event 
		#handler. For now they just have a name and a description. 
		#The event variable is just a place holder for future formatting. 
	# static = {
		# "name":"",
		# "desc":"",
		# "event":None,
		# "container":False,
		# "inventory":"",
		# "space":0
		# }
	chair = {
		"name":"chair",
		"desc":"This is a large wingback style chair upholstered in red velvet.",
		"event":None,
		"container":False,
		"inventory":[],
		"space":1
		}
	phonograph = {
		"name":"phonograph",
		"desc":"This is a cabinet style phonograph with a large hand-crank.",
		"event":None,
		"container":True,
		"inventory":[record],
		"space":1,
		}
	sofa = {
		"name":"sofa",
		"desc":"It's a Victorian style sofa with grey and dark grey vertical stripes",
		"event":None,
		"container":False,
		"inventory":"",
		"space":0,
		}
	rug = {
		"name":"rug",
		"desc":"This oriental rug has excellent knot work and patterns",
		"event":None,
		"container":False,
		"inventory":"",
		"space":0,
		}
	fireplace = {
		"name":"fireplace",
		"desc":"The brick hearth fireplace has several logs burning in it",
		"event":None,
		"container":False,
		"inventory":"",
		"space":0
		}
	piano = {
		"name":"piano",
		"desc":"It is a black baby grand piano",
		"event":None,
		"container":False,
		"inventory":"",
		"space":0
		}
	tardis = {
		"name":"tardis",
		"desc":"It's a blue policebox, it may travel in time and space",
		"event":None,
		"container":False,
		"inventory":"",
		"space":0
		}
	policebox = tardis
	police = tardis
	gear = [
		default_head,
		default_hand,
		default_body,
		default_bag,
		default_special,
		wizard_hat,
		wand,
		robes,
		satchel,
		ring_protection]
	inventory = [
		record,
		Emma,
		Tidbit,
		guitar,
		pledge,
		Noosa]
	static = [
		chair,
		phonograph,
		sofa,
		rug,
		fireplace,
		piano,
		tardis,
		policebox,
		police]
	

	
#		***	Room Classes		***
class map():
	
	class default_room(object): #parent for room classes, fills in missing info with place holders
		title = "Undefined Room"
		short_description = "A white empty room"
		long_description = [
			"This is a white nondescript space awaiting data to describe it, ",
			"Like the 'Construct' in The Matrix"
			"You don't see any obvious exits, but you think 'up' will work"
			]
		inventory = []
		static = []
		exits = {
			'up' : "Study"
			}
			
	class Study(default_room):
		#def __inti__():
		items = items()
		title = "Study"
		short_description = "A small Study"
		long_description = [
			"This is a small but cozy Study with book shelves,",
			"a wingback chair and a phonograph. Doors lead north and east"
			]
		inventory = [items.crate,items.Emma]
		static = [items.chair,items.phonograph]
		exits = {
			'north' : "Parlor",
			'east' : "Ballroom"
			}
			
	class Parlor(default_room):
		title = "Parlor"
		short_description = "It is warm and inviting here"
		long_description = [
			"This is a parlor with polished hardwood floors, an",
			"oriental rug, and a sofa facing a fireplace. Doors lead south and east"
			]
		inventory = [items.guitar,items.Tidbit]
		static = [items.sofa,items.rug,items.fireplace]
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
			"phonebooth. it has a sign on it that says 'Police Box'.",
			"Doors lead north and south"]
		inventory = [items.Noosa,items.pledge]
		static = [items.piano,items.tardis,items.policebox,items.police]
		exits = {
			'north' : "Parlor",
			'south' : "Study"
			}
	
	room_list = {
		"Study":Study(),
		"Parlor":Parlor(),
		"Ballroom":Ballroom()
		}
	starting_room = Study()

#		***	Word Lists		***

class words(object):
		
	system_commands = [
		"load",
		"save",
		"quit",
		"restart",
		"help",
		"?",
		"verbose",
		"brief",
		"score",
		"inv?",
		"q",
		"clear",
		]
		
	inventory_commands = [
		"inventory",
		"i",
		"get",
		"take",
		"equip",
		"put",
		"wear",
		"drop",
		"throw",
		"from",
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
		"enter",
		"exit",
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
		"what",
		"l",
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

#		***	Game States		***
class system():
	brief = True #True = brief description, False = Verbose
	
	rooms_visited = [] 
	
	settings = [brief,rooms_visited]
class player():
	items = items()
	inventory = [items.wand]