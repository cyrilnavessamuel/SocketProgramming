import socket
import struct

localhost = ''
port = 12800

# s is the "UDP" socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((localhost, port))
print("The server now bound on the port {}".format(port))

data = b""
while data != b"end":
    data, (HOST, PORT) = s.recvfrom(50)
    s.sendto(b"Message received",(HOST,PORT))
    # The following statement can throw an exception if the 
    # received message has special 
    print("Received {0} from client socket {1}: ".format( data, HOST))
    
print("Closing the UDP socket")
s.close()