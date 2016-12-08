def joinRoom(s): #This gets the bot in the room
	readbuffer = "" #Preps the read buffer
	Loading = True #Preps Loading
	while Loading: #Deals with twitch loading into chat
		readbuffer = readbuffer + s.recv(1024).decode() #Gets the next line and stores it in the buffer
		temp = readbuffer.split("\n") #Gets the next line that is ready to be processed
		readbuffer = temp.pop() #Removes that line that is being processed from the buffer
		
		for line in temp: #Process the message
			print(line)
			Loading = loadingComplete(line) #Checks if the loading is done
	print("Entered chat")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True
