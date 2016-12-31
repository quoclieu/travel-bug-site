from datetime import datetime,timedelta

########### TRIPS ############

#Takes in a full string date and returns only the day date
#Example: startDate = 1/2/2016, output = 1
def getDate(startDate):
	date = datetime.strptime(startDate, '%d/%m/%Y')
	return date.day

#Takes in a full string date and returns only the abbreviated month name
#Example: startDate = 1/2/2016, output = Feb
def getMonth(startDate):
	date = datetime.strptime(startDate, '%d/%m/%Y')
	return date.strftime("%b")

#Takes in a full string date and returns only the day date
#Example: startDate = 1/2/2016, output = 1
def getYear(startDate):
	date = datetime.strptime(startDate, '%d/%m/%Y')
	return date.year

#Takes in two full string dates and return a string summary of the dates
#Example startDate = 1/2/2016, endDate = 3/2/2016, output = 1-3 February
#If months are different output = 20 February - 2 March
def getFullDates(startDate,endDate):
	startDate = datetime.strptime(startDate, '%d/%m/%Y')
	endDate = datetime.strptime(endDate, '%d/%m/%Y')
	if(startDate.month == endDate.month):
		return "%s-%s %s" % (startDate.day, endDate.day, startDate.strftime("%B"))
	else:
		return "%s %s - %s %s" % (startDate.day, startDate.strftime("%B"),\
			endDate.day,endDate.strftime("%B"))

#Full date - takes in a date and an increment and return as a date number and month in format:
#eg. 19 AUG
#Example date = 1/2/2016 increment = 3 output = 4 Feb
def formatDate(date,increment):
	dateFormat = datetime.strptime(date, '%d/%m/%Y')
	dateFormat += timedelta(days=increment)
	return "%s %s" % (dateFormat.day, dateFormat.strftime("%b"))

#Takes in a date string and returns a full date
#Example date = 1/2/2016 output = 1 February 2016
def formatFullDate(date):
	dateFormat = datetime.strptime(date, '%d/%m/%Y')
	return "%s %s %s" % (dateFormat.day, dateFormat.strftime("%B"), dateFormat.year)

############ DAY ####################


#Returns the correct font awesome icon
def getIcon(transport):
	if(transport == "Train" or transport == "Tram"):
		transport_icon = "fa-train"
	elif(transport == "Car"):
		transport_icon = "fa-car"
	elif(transport == "Bus"):
		transport_icon = "fa-bus"
	elif(transport == "Taxi"):
		transport_icon = "fa-taxi"
	else:
		transport_icon = "fa-bug"
	return transport_icon

#Returns a 24 hour time into 12 hour time with AM or PM
#Takes in a timeSort string eg. 421200 converts to 12:00PM
def getTime(time):
	#get rid of the 42 at the start of the string
	time = time - 420000

	if(time-1200)>0:
		time = time-1200
		time = str(time)
		time_str = time[:-2]+':'+time[-2:]
		return(time_str+"PM")
	elif(time == 0):
		return("12:00AM")
	elif(time == 1200):
		return("12:00PM")
	else:
		time = str(time)
		time_str = time[:-2]+':'+time[-2:]
		return(time_str+"AM")




