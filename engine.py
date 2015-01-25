import os
os.system('cls')
import random
import map
import word_parser
import word_list

class engine(object): #Game loop
	#def __init__(self):
	def play(object):
		location = map.testroom1() #starting location
		room_reader = map.room_reader()
		reader = word_parser.reader() #shortcut to parser
		while True:
			print""
			room_reader.describe_room(location)			
			print ""
			#get user input, then break it down into a list of words
			action = raw_input("Which way?> ")
			action = reader.break_words(action)
			#now run the input list against a number of word checkers in the parser
			profanity = reader.profanity(action)
			location = reader.exit(action,location)
			look_at = reader.look_at(action,location)
			recognized = reader.recognized(action)
			
			

start = engine() #instantiate engine
start.play() #start game loop
