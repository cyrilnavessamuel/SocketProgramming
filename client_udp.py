import socket
import sys
import struct

if len(sys.argv) != 2:
    print("Only one argument: the dest hostname/IP address as string")
    sys.exit(2)

#Remote address
localhost = str(sys.argv[1]) #  dest hostname
#host = "localhost"
localport = 12800

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_addr = s.getsockname()
print("UDP Socket established between client socket {0} <--> server socket ({1}, {2})".format(local_addr, localhost, localport))

msg_to_send = b""
while msg_to_send != b"end":
    msg_to_send = input("> ")
    msg_to_send = bytes(msg_to_send,'utf8')
    # We send the message
    s.sendto(msg_to_send,(localhost,localport))
    (received_msg,(HOST,PORT)) = s.recvfrom(1024)
    print("Server{0} tells you {1}".format(HOST, received_msg))
print("Closing the UDP Socket")
s.close()