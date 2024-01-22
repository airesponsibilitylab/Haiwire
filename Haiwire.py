from math import random
import time
import csv

def init():
	#read incidents
	incidentsDict = {}
	with open ('Incidents.csv', mode='r') as incidentRead:
		incidentReader = csv.DictReader(incidentRead)
		for row in incidentReader:
			incidentID = row["Incident ID"]
			#deckID = row["General Deck ID"] #probably dont need
			incidentTitle = row["Card Title"]
			incidentDescription = row["Card Wording"]

	# read inject cards
	injectDict = {}
	with open("Injects.csv", mode='r') as injectRead:
		injectReader = csv.DictReader(injectRead)
		for row in injectReader:
			injectID = row["Inject ID"]
			#deckID = row["Deck ID"] #probably dont need
			injectTitle = row["Card Title"]
			injectDescription = row["Card Wording"]



#---

def roll(injectCardsRemaining):
	result = int(math.random(1,10))
	if rollResult < 7:
		haiwireCount +=1
		status = "Incident response failed, your HAIWIRE risk has increased! Please draw a new Inject card."
	elif rollResult >= 8 and rollResult <10:
		status = "Incident response partially successful, your HAIWIRE risk remains the same. Please draw a new Inject card."
	elif rollResult == 10:
		status = "HAIWIRE averted! Please draw a new Incident card."
	return status

#---

def welcome():
	"Welcome to HAIWIRE, a command-line based card game about 'AI Incidents' and how teams might react to the news.\n\nINSTRUCTIONS: One Incident Card is drawn per round. Each Card is assigned a color value that determines how many 'Inject Cards' are then drawn that you then have to individually address the consequences of as they pertain to the theme of the Incident.\n\nA Die is rolled to determine whether or not your team's 'incident response' is up to muster - Cross your fingers and hope for a 10 otherwise you risk going HAIWIRE!\n\nEach round ends once all Inject Cards for that Incident have been dealt with. The game is complete once all Incidents have been addressed.\n**--------------**\n"






#---
# def run():
# 	injectCardsRemaining = 0
# 	cardCount = len(incidentDict)

# 	if injectCardsRemaining == 0:

# 	else:
# 		rollResult = roll(injectCardsRemaining)	
# 		injectCardsRemaining -= 1
# 		print(rollResult)


#---

init()
welcome()
exit()
# run()






# This doesn't need to be "Alex thorough" for mechanics. Just "playable". It's okay if certain 
# things aren't developed/tracked in-game. It just needs to run.

# Need:
# - Random number generator to generate a whole # in the range of the amount of cards in the deck (dont need to worry about shuffling the decks if theyre all being picked via RNG)
# - timer between draws (set via input 'easy'/'medium'/'hard' - default 'Medium' w/ empty string enter)
		# ASK RAMSAY ABOUT THE DIFFICULTY/TIME PER INJECT
# - We're going with a specific # of incidents to track progress in the game/"when does the game end"
# - Game status:
# 		- round counter / checks at the end of each round to see if that's the last round
# - 2 dictionary of objects:
#	 	Incident Card Dict:
# 			- Unique card #ID
# 			- Bool to track if its been drawn already
#	 		- Color (R/Y/G) corresponding to the "inject card" value/count (int 2-4)
# 			- Description
# 		Inject Card Dict:
# 			- Unique Inject card #ID
# 			- Bool to track if its been drawn already (are these single-use?)
# 			- Description


# Game steps:
- start game
- "press enter to draw an incident card"
- read card to CLI, reset inject counter, determine inject card count and print the inject count
- input stop
- press enter to draw inject card, increment counter, print card to CLI
- begin 2 minute timer
- input stop
- prompt player to hit enter to roll a die
- generate random # 1-10
- display result