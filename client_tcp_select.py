import socket
import select
import sys

if len(sys.argv) != 2:
    print("Only one argument: the dest hostname/IP address as string")
    sys.exit(2)

#Remote address
host = str(sys.argv[1]) #  dest hostname
#host = "localhost"

port=12800

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
   socket.connect((host,port))
except socket.gaierror:
    print("The argument must be a valid hostname or a port")
    sys.exit(2)
local_addr = socket.getsockname()
print("Connection established between client socket {0} <-----> server socket ({1},{2})".format(local_addr,host,port))

inputarray = [socket]


while 1:
    inputs,outputs,errors= select.select(inputarray,inputarray,[],5)
    #if (len(inputs)!=0):
                      #buffer = socket.recv(1024)
                      #if len(buffer)!=0:
                          #print ("received data:"+str(buffer))
    if (len(outputs)!=0):
                       msg_to_send=b""
                       while msg_to_send!=b"end":
                           msg_to_send = input("> ")
                           msg_to_send = msg_to_send.encode()
                           socket.send(msg_to_send)

