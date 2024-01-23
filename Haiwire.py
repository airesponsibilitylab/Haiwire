import random
import time
import csv

def init():
	#read incidents
	incidentsList = []
	with open ('Incidents.csv', mode='r') as incidentRead:
		incidentReader = csv.DictReader(incidentRead)
		for row in incidentReader:
			incidentsDict = {}
			incidentsDict["Incident ID"] = row["General Deck ID"]
			incidentsDict["Incident Title"] = row["Card Title"]
			incidentsDict["Incident Description"] = row["Card Wording"]
			incidentsDict["Incident Tech"] = row["AI Stack"]
			incidentsDict["Incident Domain"] = row["Domain"]
			incidentsDict["Incident Harm"] = row["Harm"]
			incidentsDict["Incident Color"] = row["Card Color"]
			if row["Card Color"] == "GREEN":
				incidentsDict["Incident Inject Count"] = 2
			elif row["Card Color"] == "AMBER":
				incidentsDict["Incident Inject Count"] = 3
			elif row["Card Color"] == "RED":
				incidentsDict["Incident Inject Count"] = 4
			incidentsList.append(incidentsDict)

	# read inject cards
	injectList = []
	with open("Injects.csv", mode='r') as injectRead:
		injectReader = csv.DictReader(injectRead)
		for row in injectReader:
			injectDict = {}
			injectDict["Inject ID"] = row["Deck ID"]
			injectDict["Inject Title"] = row["Card Title"]
			injectDict["Inject Wording"] = row["Card Wording"]
			injectList.append(injectDict)

#DONE

#---

def welcome():
	print("Welcome to HAIWIRE, a command-line based card game about 'AI Incidents' and how teams might react to the news.\n\nINSTRUCTIONS: One Incident Card is drawn per round. Each Card is assigned a color value that determines how many 'Inject Cards' are then drawn that you then have to individually address the consequences of as they pertain to the theme of the Incident. You have two minutes to come up with a plan for each Inject Card before the Die is rolled. \n\nA Die is rolled to determine whether or not your team's 'incident response' is up to muster - Cross your fingers and hope for a 10 otherwise you risk going HAIWIRE!\n\nEach round ends once all Inject Cards for that Incident have been dealt with. The game is complete once all Incidents have been addressed.\n\n**--------------**\n")

#Done

#---

def roll():
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

def drawIncident():
	ID = int(random.randrange(1,20))
	for datadict in incidentsList:
		if datadict["Incident ID"] == ID:
			ID = index(datadict["Incident ID"])
			ID = index(datadict["Inject ID"])
			incidentData = incidentsList.pop(ID)
			return incidentData
		else:
			return None
#DONE

#---

def drawInject():
	ID = int(random.randrange(1,40))
	for datadict in injectList:
		if datadict["Inject ID"] == ID:
			ID = index(datadict["Inject ID"])
			injectData = injectList[ID]
			return injectData

#DONE

#---
def run():
	deckTotal = len(incidentsList)
	while deckTotal > 0:
		deckTotal -= 1
		
		#start round
		incidentData = None
		while incidentData == None:
			incidentData = drawIncident()
		print("Incident Title: {}\n".format(incidentData["Incident Title"]))
		print("Incident Description: {}\n".format(incidentData["Incident Description"]))
		print("Incident Technology: {}\n".format(incidentData["Incident Tech"]))
		print("Incident Domain: {}\n".format(incidentData["Incident Domain"]))
		print("Incident Harm: {}\n\n".format(incidentData["Incident Harm"]))
		print("Incident Severity: {}".format(incidentData["Incident Color"]))
		print()
		injectTotal = incidentData["Incident Inject Count"]
		print("Discuss your Response Plan and then draw {} injects. Press 'Enter/Return' to draw an Inject Card.\n\n\n".format(str(injectTotal)))
		input = ""
		
		#start inject card draw
		injectCount = 0
		while injectCount < injectTotal:
			injectData = drawInject()
			injectCount+=1
			print("Inject Card Title: {}".format(injectData["Inject Title"]))
			print("Inject Card Description: {}".format(injectData["Inject Wording"]))
			print()
			print("Discuss the Inject Card, updating or reformulating your response strategy. You have two minutes starting *now*.")
			time.sleep(120)
			print()

			#roll
			injectRemaining = injectTotal - injectCount #4-1 = 3
			roll(injectCardsRemaining)



		print(rollResult)


#---

init()
welcome()
run()






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

# - input stop
# - prompt player to hit enter to roll a die
# - generate random # 1-10
# - display result