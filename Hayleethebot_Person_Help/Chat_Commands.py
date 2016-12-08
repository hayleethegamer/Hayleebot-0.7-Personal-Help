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
    
import Functions

def chatCommands(messageObj,s):
	if messageObj.message.lower().startswith("!credit"): #The format for a command, replace ! with whatever you want that is not a letter, credits is the command name
		#messageObj.message is the message, .lower() makes it all lower case, .startswith() checks if the string (in this case messageObj.message) starts with what's in the ()
		Functions.sendMessage(s,"I would like to thank Hayleethegamer for helping me, here is the link to the code: https://github.com/hayleethegamer/Hayleebot-Personal-Help")
