import sys
from playsound import playsound
#Source: https://www.geeksforgeeks.org/play-sound-in-python/
#WAV:
	#playsound('/path/note.wav')
	#print('playing sound using playsound')
#mp3:
	#playsound('/path/note.mp3')
	#print('playinbg sound using playsound')
#Setting the arguement block to False to make the function run asynchonously

world = {

}

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

def render(current_location, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Total moves: " + str(moves))
		print("You are located at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")


def get_input():
	response = input("What now? ")
	response = response.upper().strip()
	return response


def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"].upper() == response:
				return link["passageName"]
	print("Please try again.")
	return location_label
#

#############location_label = "[First Area]"
current_location = {}
response = ""
moves = 0

while True:
	if response == "QUIT":
		break
	moves =+ 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	render(current_location, moves)
	response = get_input()

print("End")