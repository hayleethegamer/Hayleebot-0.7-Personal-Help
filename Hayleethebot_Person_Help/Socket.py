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