import socket

# Client configuration
server_host = '127.0.0.1'
server_port = 12345

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))
print("Connected to the server on", server_host, "port", server_port)

# Receive data from the server and simulate client's ACKs
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break

    print("Client received data:", data)
    # Simulate an ACK by sending an empty response to the server
    client_socket.send("ACK".encode())

client_socket.close()
