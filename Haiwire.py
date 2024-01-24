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
			incidentsDict["Incident ID"] = int(row["General Deck ID"])
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
			injectDict["Inject ID"] = int(row["Deck ID"])
			injectDict["Inject Title"] = row["Card Title"]
			injectDict["Inject Wording"] = row["Card Wording"]
			injectList.append(injectDict)

	return incidentsList,injectList

#DONE

#---

def welcome():
	print("Welcome to HAIWIRE, a command-line based card game about 'AI Incidents' and how teams might react to the news.\n\nINSTRUCTIONS: One Incident Card is drawn per round. Each Card is assigned a color value that determines how many 'Inject Cards' are then drawn that you then have to individually address the consequences of as they pertain to the theme of the Incident. You have two minutes to come up with a plan for each Inject Card before the Die is rolled. \nA Die is rolled to determine whether or not your team's 'incident response' is up to muster - Cross your fingers and hope for a 10 otherwise you risk going HAIWIRE!\n\nEach round ends once all Inject Cards for that Incident have been dealt with. The game is complete once all Incidents have been addressed.\n\n**--------------**")
	time.sleep(10)
#Done

#---

def roll():
	rollResult = int(random.randrange(1,10))
	time.sleep(2)
	print("You rolled a {}".format(str(rollResult)))
	time.sleep(1)
	statusMessage = "fmndklgmdfgkld FAILURE AT STATUS MESSAGE"
	if rollResult < 7:
		haiwireVal = 1
		statusMessage = "Incident response failed, your HAIWIRE risk has increased! Press 'Enter/Return' to draw a new Inject Card."
	elif rollResult >= 7 and rollResult <10:
		statusMessage = "Incident response partially successful, your HAIWIRE risk remains the same. Press 'Enter/Return' to draw a new Inject Card."
		haiwireVal = 0
	elif rollResult == 10:
		statusMessage = "Inject Card catastrophe averted! Press 'Enter/Return' to draw a new Inject Card."
		haiwireVal = -1
	else:
		return

	# time.sleep(1)
	return statusMessage, haiwireVal



#---

def drawIncident():
	ID = int(random.randrange(1,21))
	for index, datadict in enumerate(incidentsList):
		if ID == int(datadict["Incident ID"]):
			incidentData = incidentsList.pop(index)
			return incidentData
		else:
			return None
#DONE

#---

def drawInject():
	ID = int(random.randrange(1,41))
	for index, datadict in enumerate(injectList):
		if ID == int(datadict["Inject ID"]):
			injectData = datadict
			return injectData

#DONE

#---
def run(incidentsList,injectList):
	time.sleep(1)
	deckTotal = len(incidentsList)
	current = 0
	while deckTotal > 0:
		haiwireCount = 0
		deckTotal -= 1
		current +=1
		print("Round {}!".format(str(current)))
		#start round
		incidentData = None
		while incidentData == None:
			incidentData = drawIncident()
		print("Incident Title: {}".format(incidentData["Incident Title"]))
		print("Incident Description: {}".format(incidentData["Incident Description"]))
		print("Incident Technology: {}".format(incidentData["Incident Tech"]))
		print("Incident Domain: {}\n".format(incidentData["Incident Domain"]))
		print("Incident Harm: {}".format(incidentData["Incident Harm"]))
		print("Incident Severity: {}".format(incidentData["Incident Color"]))
		print()
		injectTotal = incidentData["Incident Inject Count"]
		print("Discuss your Response Plan and then draw {} injects. Press 'Enter/Return' to draw an Inject Card.\n**-------**".format(str(injectTotal)))
		stop = input("")
		time.sleep(1)
		
		#start inject card draw
		injectCount = 0
		while injectCount < injectTotal:
			time.sleep(1)
			injectData = drawInject()
			injectCount+=1
			print("Inject Card Title: {}".format(injectData["Inject Title"]))
			print("Inject Card Description: {}".format(injectData["Inject Wording"]))
			print()
			print("Discuss the Inject Card and update or reformulate your response strategy. Press 'Enter/Return' to roll a Die: \n")
			stop = input("")
			print("Rolling a Die!")
			statusMessage,haiwireVal = roll()
			haiwireCount += 1
			if haiwireVal == -1:
				print(statusMessage)
				break
			elif haiwireVal == 0:
				print(statusMessage)
				print
			elif haiwireVal == 1:
				print(statusMessage)
				if haiwireCount == injectTotal:
					print("You lose the round! Your org has gone HAIWIRE!!")
			print("\n**-------**\n")
			stop = input("")
			if haiwireCount == injectTotal:
				time.sleep(1)
				print("Round over, your HAIWIRE score was: {} of {} points".format(haiwireCount,injectTotal))
				break
		print()
		print("\n\n**--------------**")
	time.sleep(5)
	print("\n\n**--------------**")
	print("Game over! Thanks for playing!\n\n")
	print("\n\n**--------------**")
	time.sleep(5)

#---

while True:
	incidentsList,injectList = init()
	welcome()
	run(incidentsList,injectList)
	exit()
