import socket
#socket is module to create socket
server_socket = socket.socket()
#creating server side sockets
host = socket.gethostbyname(socket.gethostname())
#host name will active ip on server 
#gethostbyname -> will give ip of a hostname
#gethostname -> hostname of current system
port = 12345

server_socket.bind((host,port))

server_socket.listen()
print("SERver is listing to clients ")
client_socket,client_addr = server_socket.accept()
print("Got connection from ",*client_addr)
while True :
    msg = input("server->")
    client_socket.send(msg.encode())
    if msg == 'bye' :
        client_socket.close()
        server_socket.close()
        break
    cmsg = client_socket.recv(1024).decode()
    print("\t\t\tClient->",cmsg)
