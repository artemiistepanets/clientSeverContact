#this code is not very different from part 1 and 2
# client is cretes, tehn connected to the server where it sends a packet of the guess fpr the row and column.
# then it sends that guess and receives if the guess was right or wrong.
from socket import *
serverName = '10.21.204.234'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input your row guess followed directly by your column guess (without spaces): ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()
