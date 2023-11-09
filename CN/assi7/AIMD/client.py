import socket
import time

# Client configuration
server_host = '127.0.0.1'
server_port = 12345

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))
print("Connected to the server on", server_host, "port", server_port)

try:
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print("Client received data:", data)
        # Simulate an ACK by sending an empty response to the server
        client_socket.send("ACK".encode())
        time.sleep(1)  # Simulate a round-trip time

except KeyboardInterrupt:
    pass

client_socket.close()
