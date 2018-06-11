import socket

server_socket = socket.socket()
host = socket.gethostbyname(socket.gethostname())
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
