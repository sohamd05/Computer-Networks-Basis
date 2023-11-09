import socket
import threading

# Global variables
HOST = 'localhost'
PORT = 12345
clients = {}

# Function to broadcast messages to all clients
def broadcast(message, sender_name):
    for name, client_socket in clients.items():
        if name != sender_name:
            try:
                client_socket.send(message)
            except:
                # Remove the client if unable to send the message
                del clients[name]

# Function to handle incoming messages from clients
def handle_client(client_socket, client_name):
    try:
        while True:
            message = client_socket.recv(1024)
            if message:
                broadcast_message = f"{client_name}: {message.decode('utf-8')}"
                print(broadcast_message)
                broadcast(broadcast_message.encode('utf-8'), client_name)
            else:
                break
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        del clients[client_name]
        leave_message = f"{client_name} has left the chat."
        print(leave_message)
        broadcast(leave_message.encode('utf-8'), client_name)
        client_socket.close()

# Main server function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Chat room server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, addr = server.accept()
            client_name = client_socket.recv(1024).decode('utf-8')
            clients[client_name] = client_socket

            join_message = f"{client_name} has joined the chat."
            print(join_message)
            broadcast(join_message.encode('utf-8'), client_name)

            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_name))
            client_handler.start()

    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server.close()

if __name__ == '__main__':
    main()
