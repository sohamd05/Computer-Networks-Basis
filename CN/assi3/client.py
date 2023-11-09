##Client 

import socket

# Define server address and port
server_ip = "127.0.0.1"  # Use the same server IP as in server.py
server_port = 12345       # Use the same server port as in server.py

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to server at {server_ip}:{server_port}")

while True:
    # Get user input
    user_message = input("You: ")

    # Send the user's message to the server
    client_socket.send(user_message.encode("utf-8"))

    # Receive and display the server's response
    server_response = client_socket.recv(1024).decode("utf-8")
    print(f"Server says: {server_response}")

# Close the client socket
client_socket.close()
