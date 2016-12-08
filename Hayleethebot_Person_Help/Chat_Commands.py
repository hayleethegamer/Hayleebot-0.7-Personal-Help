import Functions

def chatCommands(messageObj,s):
	if messageObj.message.lower().startswith("!credit"): #The format for a command, replace ! with whatever you want that is not a letter, credits is the command name
		#messageObj.message is the message, .lower() makes it all lower case, .startswith() checks if the string (in this case messageObj.message) starts with what's in the ()
		Functions.sendMessage(s,"I would like to thank Hayleethegamer for helping me, here is the link to the code: https://github.com/hayleethegamer/Hayleebot-Personal-Help")