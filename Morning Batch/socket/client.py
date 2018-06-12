import socket

server_socket = socket.socket()
host = socket.gethostbyname(socket.gethostname()) # Give server address if server is on differnt machine
port = 12345 #port no on which server is listing 

server_socket.connect((host,port))
print("Got Connection from server at {}:{} ".format(host,port))
while True :
    smsg = server_socket.recv(1024)
    if smsg.decode().strip().lower() == 'bye' :
        print("Connection is Terminated by server")
        server_socket.close()
        break
    print("\t\t\tServer -> ",smsg.decode())
    msg = input("client->")
    server_socket.send(msg.encode())
    if msg == 'bye' :
        server_socket.close()
        break
