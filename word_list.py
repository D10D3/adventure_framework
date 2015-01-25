
class words(object):
		
	test_words = [
		"test",
		"words",
		"are",
		"being",
		"read"]

	nav_command = [
		"north",
		"south",
		"east",
		"west",
		"fore",
		"aft",
		"starboard",
		"port",
		"up",
		"down",
		"f",
		"a",
		"s",
		"p"
		]
	
	verbs = [
		"go",
		"enter",
		"get",
		"take",
		"equip",
		"put on",
		"wear",
		"quit",
		"climb",
		"g",
		"put",
		"turn",
		"turn on",
		"turn off",
		"move",
		"attack",
		"kill",
		"break",
		"inventory",
		"eat",
		"drink",
		"shout"
		"drop",
		"restart",
		]

	describers = [
		"look",
		"read",
		"examine",
		"describe",
		"scan",
		"what"
		]
		
	profanity = [
		"fuck",
		"fucker",
		"motherfucker"
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
		"douche",
		]

	wordlists = [
		test_words,
		nav_command,
		verbs,
		describers,
		profanity,
		]
		
	items = {
	"spacesuit" : "this is a standard utility suit for working in a vacuum",
	"keycard" : "This is the keycard to the flight Deck",
	"toolkit" : "This is a sturdy box containing all of the tools and supplies for maintenance and repair",
	"medkit" : "This state of the art medkit has emergency supplies for treating wounds"
	}
	
	""" Commands stolen from Zork:
			Move commands
		Command 	Shortcut 	Action
		north 	n 	Move north
		south 	s 	Move south
		east 	e 	Move east
		west 	w 	Move west
		northeast 	ne 	Move northeast
		northwest 	nw 	Move northwest
		southeast 	se 	Move southeast
		southwest 	sw 	Move southwest
		up 	u 	Move up
		down 	d 	Move down
		look 	l 	Looks around at current location
		save 		Save state to a file
		restore 		Restores a saved state
		restart 		Restarts the game
		verbose 		Gives full description after each command
		score 		Displays score and ranking
		diagnostic 		Give description of health
		brief 		Give a description upon first entering an area
		superbrief 		Never describe an area
		quit 	q  	Quit game
		climb 		climbs(up)
		g 		last common
		go(direction) 		go towards direction(west/east/north/south/in/out/into)
		in/into 		in to the place(window,...)
		out 		go out of the place(kitchen,...)
		hi/hello 		say hello...
		fuck/shit/damn 		Random Comment e.g. : Such language in a high-class establishment like this!
		i 		inventory
		(None)		I beg your pardon?
		Item commands
		Command (Argument) 	Action
		get/take (item) 	Removes item from current room; places it in your inventory
		get/take all 	takes all takeable objects in room
		throw (item) at (location) 	Throws the item at something
		open (container) 	Opens the container, whether it is in the room or your inventory
		open (exit) 	Opens the exit for travel
		read (item) 	Reads what is written on readable item
		drop (item) 	Removes item from inventory; places it in current room
		put (item) in (container) 	Removes item from inventory; places it in container
		turn (control) with (item) 	Attempts to operate the control with the item
		turn on (item) 	Turns on the item
		turn off (item) 	Turns the item off
		move (object) 	Moves a large object that cannot be picked up
		attack (creature) with (item) 	Attacks creature with the item
		examine (object) 	Examines, or looks, at an object or item or location
		inventory 	Shows contents of Inventory
		eat 	Eats item (specifically food)
		shout 	Aaaarrrrgggghhhh!
		close [Door] 	Closes door
		tie (item) to (object) 	
		pick (item) 	take/get item
		kill self with (weapon) 	Humorously commits suicide
		break (item) with (item) 	Breaks item
		kill (creature) with (item) 	  Attacks creature with the item
		pray 	 when you are in temples...
		drink 	drink an item
		"""



