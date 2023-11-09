##Server

import socket

# Define server address and port
server_ip = "127.0.0.1"  # Use "localhost" or your actual server IP
server_port = 12345

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (up to 5 clients)
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

while True:
    # Receive data from the client
    client_message = client_socket.recv(1024).decode("utf-8")
    if not client_message:
        break

    print(f"Client says: {client_message}")

    # Send a response back to the client
    server_response = input("Enter your reply: ")
    client_socket.send(server_response.encode("utf-8"))

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
