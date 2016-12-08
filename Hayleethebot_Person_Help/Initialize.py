'''Copyright (C) 2016 Hayleethegamer 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''
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
