import socket
import select

host=''
port=12800

socket=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket.bind((host,port))
socket.listen(1)

#creating input array to be passed to select function for incoming, outgoing and error data
inputarray = [socket]

while 1:
         inputs,outputs,errors = select.select(inputarray,inputarray,[],5)
         if (len(inputs)!= 0):
             i=0
             for input in inputs:
                 if(i<len(inputs)):
                   if input is socket:
                     clientsocket,clientaddress = input.accept()
                     inputarray.append(clientsocket)
                   else:
                     data=input.recv(1024)

                     if not data:
                         inputarray.remove(input)
                     else:
                         print ("This is the client data"+str(data))
                 i=i+1

