# File: ServerHomework1
# Author: Mitchell Noun
# Class: COMP430-001
# Directory test file: http://127.0.0.1:80/Users/mitchellnoun/PycharmProjects/COMP430_Homework1_Noun/HelloWorld.txt

#import socket module
from socket import *
import sys  # In order to terminate the program

'# Create a TCP server socket'
'#(AF_INET is used for IPv4 protocols)'
'#(SOCK_STREAM is used for TCP)'
serverSocket = socket(AF_INET, SOCK_STREAM)

'#Prepare a sever socket'
'#Fill in start'
serverPort = 80
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
'#Fill in end'

while True:
    '#Establish the connection'
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start ... #Fill in end
    try:
        '# Receives the request message from the client'
        message = connectionSocket.recv(1024)  # Fill in start .. #Fill in end
        filename = message.split()[1]
        f = open(filename)

        '# Store the entire content of the requested file in a temporary variable'
        outputdata = f.read()  # Fill in start ... #Fill in end

        '# Send one HTTP header line into socket'
        '# Fill in start ...'
        connectionSocket.send("\nHTTP/1.1 200 OK\n\n")
        '# Fill in end'

        '#Send the content of the requested file to the client'
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        '#Send response message for file not found'
        '#Fill in start ...'
        connectionSocket.send("\nFile Not Found\n")
        '#Fill in end'

        '#Close client socket'
        '#Fill in start ...'
        connectionSocket.close()
        '#Fill in end'
        serverSocket.close()
        '#Terminate the program after sending the corresponding data'
        sys.exit()