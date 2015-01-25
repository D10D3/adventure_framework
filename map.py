
class room_reader(object):
	def describe_room(self,location):
		self.location = location
		print location.data['title']
		print location.data['short_description']
		print""
		item_list = "Items here: "
		for key in location.inventory.keys():
			item_list += key
			item_list += ", "
		print item_list
		
		objects_list = "Objects here: "
		for key in location.objects.keys():
			objects_list += key
			objects_list += ", "
		print objects_list
		
		exits_list = "Exits: "
		for key in location.exits:
			exits_list += key
			exits_list += ", "
		print exits_list
	
		
class testroom1(object):
	data = {
		"title" : "testroom1",
		"short_description" : "This is testroom1, It's clean",
		}
	inventory = {
		"stool":"a simple wooden stool",
		"Emma":"a very grumpy cat"
		}
	objects = {
		"car":"A 1985 Buick Grand National",
		"futon":"A cheap futon from ikea"
		}
	exits = ['north','east']

	def transition(self,exit):
		self.exit = exit
		if exit == 'north':
			location = testroom2()
		else:
			location = testroom3()
		return location
		
class testroom2(object):
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
		
class testroom3(object):
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
