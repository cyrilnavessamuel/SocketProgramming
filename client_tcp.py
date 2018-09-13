import socket
import sys

if len(sys.argv) != 2:
    print("Only one argument: the dest hostname/IP address as string")
    sys.exit(2)

#Remote address
host = str(sys.argv[1]) #  dest hostname
#host = "localhost"
port = 12800

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:                                
    s.connect((host, port))
except socket.gaierror:          
    print("The argument must be a valid dest hostname/IP address ")                       
    sys.exit(2)  
#print("Connection established with server {0} on port {1}".format(host, port))
local_addr = s.getsockname()
print("Connection established between client socket {0} <--> server socket ({1}, {2})".format(local_addr, host, port))

msg_to_send = b""
while msg_to_send != b"end":
    msg_to_send = input("> ")
#    msg_to_send = raw_input("> ")
    # Can crash if you type special characters
    msg_to_send = msg_to_send.encode()
    # We send the message
    s.send(msg_to_send)
    received_msg = s.recv(1024)
    received_msg = received_msg.decode()
    remote_addr = s.getpeername()
    print("Server{0} tells you {1}".format(remote_addr, received_msg))    
    # Again, can crash if there are accents
print("Closing the connection")
s.close()