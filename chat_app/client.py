import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
host = socket.gethostname()
port = 9999
client_socket.connect((host, port))
print("Connected to server")

while True:
    # Send message to server
    client_msg = input("Client: ")
    client_socket.send(client_msg.encode())

    # Receive server reply
    server_msg = client_socket.recv(1024).decode()
    print("Server:", server_msg)
