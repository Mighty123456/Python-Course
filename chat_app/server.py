import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to host and port
host = socket.gethostname()
port = 9999
server_socket.bind((host, port))

# Listen for connection
server_socket.listen(1)
print("Server is waiting for connection...")

# Accept client connection
connection, address = server_socket.accept()
print("Connected with:", address)

while True:
    # Receive message from client
    client_msg = connection.recv(1024).decode()
    print("Client:", client_msg)

    # Enter reply to send to client
    server_msg = input("Server: ")
    connection.send(server_msg.encode())
