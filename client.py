import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("172.22.66.47",55555)
print(f'connectin to {server_address}')
a=s.connect_ex(server_address)
print(a)


