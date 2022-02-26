from socket import *
import sys
import random
import numpy as np

# creates the grid, randomly generates the placement of the star, and prints the array for the server to see
theGrid = [["", "", ""],
           ["", "", ""],
           ["", "", ""]]
X = random.randint(0,2)
Y = random.randint(0,2)
theGrid[X][Y] = "*"
print(np.array(theGrid))

#the following commands until the while loop creates the server connection and starts to listen
serverName = '10.21.204.234'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
#in the while loop, the server receives the messages, checks it against the x and y values randomly produces, and sends back a message if the guess is right or wrong
while True:
    connectionSocket, add = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print("The guessed x value: "+ str(int(sentence[:1])-1) + " the y value: " + str(int(sentence[1:])-1))
    print(sentence)
    if X == int(sentence[:1])-1 and Y == int(sentence[1:])-1:
        mes = "You found me, my friend at Position" + str(sentence)
        connectionSocket.send(mes.encode())
    else:
        connectionSocket.send("Nope, I’m not there".encode())
    connectionSocket.close()
