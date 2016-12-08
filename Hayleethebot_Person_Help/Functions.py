import datetime
from settings import CHANNEL

def sendMessage(s, message): #This is a function to call so you don't have to put all the code below every time you wanna send a message to twitch
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message + "\r\n" #gets message in a formate twitch will accept
	s.send(messageSend.encode('utf-8')) #Sends the message
	print(getTime() + " BotName: " + messageTemp) #Prints the message to the console

def getMessage(line): #Gets the user, message, and tags
	split = line.split(" :", 2) #splits the message up
	user = split[1].split("!", 1)[0] #gets the user
	try: #gets the message, if there is no message, makes it a blank string
		message = split[2] 
	except IndexError:
		message = ""
	tags = split[0]
	tags = tags.split(";")
	tagdict = {}
	for tag in tags:
		t = tag.split("=")
		if t[1].isnumeric():
			t[1] = int(t[1])
			tagdict[t[0]] = t[1]
	tags = tagdict
	
	messageObj = MessageOject(user, message, tags)
	return messageObj

def getMessageNoTags(line): #use this if you don't use tags
	split = line.split(" :", 2) #splits the message up
	user = split[0].split("!", 1)[0] #gets the user
	try: #gets the message, if there is no message, makes it a blank string
		message = split[1] 
	except IndexError:
		message = ""
	
	messageObj = MessageOject(user, message, tags)
	return messageObj

def getTime(): #Gets the current time in a neat string format
    now = datetime.datetime.now()
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    time = (month + "" + day + "" + year + "" + hour + "" + ":" + minute + ":" + second)
    return time


class  MessageObject: #a neat package
    def _init_(self,user,message,tags):
        self.user = user
        self.message = message
        self.timestamp = datetime.datetime.now()
        self.tags = tags