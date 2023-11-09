import socket
import threading

# Global variables
HOST = 'localhost'
PORT = 12345

# Function to receive messages from the server
def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client_socket.close()

# Main client function
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_name = input("Enter your name: ")
    client_socket.send(client_name.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == "exit":
            break
        client_socket.send(message.encode('utf-8'))

if __name__ == '__main__':
    main()
