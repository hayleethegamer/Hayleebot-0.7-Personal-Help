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
import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL #Imports all the variables from settings

def openSocket():
	s = socket.socket() #Makes a socket
	s.connect((HOST, PORT)) #Creates the connection to twitch
	sendPass = "PASS " + PASS + "\r\n" #gets the Authcode ready to send to twtich
	sendNick = "NICK " + IDENT + "\r\n" #gets the Bot's Name ready to send to twtich
	sendJoin = "JOIN #" + CHANNEL + "\r\n" #gets the Channel to join ready to send to twtich
	s.send(sendPass.encode('utf-8')) #These send the stuff above to twich
	s.send(sendNick.encode('utf-8'))
	s.send(sendJoin.encode('utf-8'))
	return s #Returns the socket so it can be used else where
