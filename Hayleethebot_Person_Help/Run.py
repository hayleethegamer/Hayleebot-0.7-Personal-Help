from Socket import openSocket
from Initialize import joinRoom
from Chat_Commands import chatCommands
import Functions
import sys

s = openSocket()
joinRoom(s)
readbuffer = ""

stopped = 0
errors = 0
osError = False


def runChat(): #The funciton that handles chat
	global readbuffer #lets the function edit the readbuffer
	global osError #For for the OSError exception below
	while True: #Makes an infinit loop
		try:
			readbuffer = readbuffer + s.recv(1024).decode() #Same as when it was in Initalize
			temp = readbuffer.split("\n")
			readbuffer = temp.pop()
			for line in temp:
				if line.startswith("PING"): #If the line is a ping, respond to it with PONG
					s.send(line.replace("PING", "PONG"))
					print(getTime() + " " + line)
					print(getTime() + " " + line.replace("PING", "PONG"))
					sendMessage(s, "Debug: Ping found and responded too") #This is to fix an issue, if this actually gets to chat remove this line
					continue
				messageObj = Functions.getMessage(line) #gets the user message and tags in a neat package, use the other one if no tags are used
				chatCommands(messageObj,s) #calls the main commands file
		except KeyboardInterrupt: #If you hit CTRL + C this happens
			Functions.sendMessage(s, "OK leaving now.") #tells chat the bot is leaving, optional
			sys.exit() #stops the code
		except (PermissionError, FileNotFoundError, FileExistsError): #This happens if there a file is not found, exists, or you don't have permissiosn to it
			errorHandleing("There was a permissions Error or the file was not found or the file exists already, i do not have the rights to access this file.")
		except OSError: #This happens in a generic OSError, I had spam issues with this error
			if osError == False: #checks if there was already an OSError
				osError = True #makes it so there was an OSError
				Functions.sendMessage(s, "There was an OSError") #says an OSError happened
				while True:
					sys.exit(2) #Tries to kill the bot until it dies
		except:
			errorLen = len(sys.exc_info()) #Checks how long the error is
			errorMessage = str(sys.exc_info()[0:errorLen]) #makes the entire error into a string
			errorHandleing(errorMessage) #Handles the Error

def errorhandleing(errorMessage): #Handles most Errors
    global errors
    global stopped
    errors += 1 #Sets errors to be one more then it was previously
    if (errors >= 5) and (stopped == False): #checks if to many errors have been sent
        Functions.sendmessage(s,"bruh, chill with these errors")
        stopped = True
        sys.exit()
    elif errors <= 5: #If not to many errors have already been sent
        Functions.sendMessage(s,errorMessage)
        print(traceback.format_exe()) #Prints the full traceback to console for Debugging