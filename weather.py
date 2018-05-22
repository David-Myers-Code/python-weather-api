'''
David Myers

API key: 3c198c6d0ce8a442

'''
import urllib2
import json

#error messages for  inputs
class BadCity (Exception):
	def __str__ (self):
		return "Bad city was entered.  Try again."

class BadState (Exception):
	def __str__ (self):
		return "Bad state was entered.  Try again."

#function to get name of city
def getCity():
	city = raw_input("Enter the name of the city:  ")
	if city:
		city = city.title()
		city = city.replace(" ","_")
		return city
	else:
		raise BadCity()
		return	

#function to get name of state
def getState():
	state = raw_input("Enter the initials of the state:  ")
	if state:
		state = state.upper()[0:2]
		return state
	else:
		raise BadCity()
		return	

#main function
def main():
	#get city and state
	city = getCity()
	state = getState()
	#web site api key
	APIKEY = "3c198c6d0ce8a442"
	
	weatherURL = "http://api.wunderground.com/api/{}/conditions/q/{}/{}.json".format(APIKEY, state, city)
	#process data from url
	url = urllib2.urlopen(weatherURL)
	theJSON = url.read()
	weather = json.loads(theJSON)
	w = weather["current_observation"]
	
	#weather output
	print "Weather report for {}, {}:".format(city, state)
	print "Temperature (F): {}".format(w["temp_f"])
	print "Temperature (C): {}".format(w["temp_c"])
	print "Right now the weather is {}".format(w["weather"])
	print "The wind speed is {} mph".format(w["wind_mph"])

	
main()	