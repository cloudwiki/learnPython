import socket

s = socket.socket()
host = socket.gethostname() #the server host, for simplicity, server/client running on the same server
port = 1234 #server port

s.connect((host, port)) #Connect the socket to a remote address. 
print s.recv(1024)

