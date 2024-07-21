import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("172.22.66.47",55555)
s.bind(server_address)
s.listen(1)
while 1:
    print("waiting for connection")
    connection,client_address=s.accept()
    print(f'recieved a connection from {client_address}')



