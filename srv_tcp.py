import socket

host = ''
port = 12800

# s is the "listenning" socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("The server now listens on the port {}".format(port))

# conn is the "service socket" object
conn, remote_addr= s.accept()
local_addr = conn.getsockname()
print("The server is now connected to the client socket {0} using the server socket {1}".format(remote_addr, local_addr))

received_msg = b""
while received_msg != b"end":
    received_msg = conn.recv(1024)  
    conn.send(b"Message received")
    # The following statement can throw an exception if the 
    # received message has special 
    print("Received {0} from client socket {1}: ".format( received_msg.decode(), remote_addr))    
    
print("Closing the connection")
conn.close()
s.close()