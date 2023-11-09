import socket

# Server configuration
server_host = '127.0.0.1'
server_port = 12345

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(1)

print("Server listening on", server_host, "port", server_port)

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Accepted connection from", client_address)

# AIMD simulation
congestion_window = 1
threshold = 8
i =0 
try:
    while i < 20 :
        print("Server: Congestion window =", congestion_window)
        client_socket.send(str(congestion_window).encode())
        ack = client_socket.recv(1024).decode()

        if congestion_window >= threshold:
            congestion_window //= 2
        else:
            congestion_window += 1
        i+=1 

except KeyboardInterrupt:
    pass

print("AIMD simulation finished.")
client_socket.close()
server_socket.close()
