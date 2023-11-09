import socket
import hashlib

def receiver():
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)  # Change to the receiver's address and port

    receiver_socket.bind(receiver_address)

    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        packet = data[:-16]  # Remove the last 16 bytes (checksum)
        checksum = data[-16:]  # Get the last 16 bytes as the checksum

        # Calculate checksum for error checking
        calculated_checksum = hashlib.md5(packet).digest()

        if calculated_checksum == checksum:
            print(f"Received valid message: {packet.decode()}")
            receiver_socket.sendto(b'ACK', sender_address)
        else:
            print("Received a corrupt message. Sending NACK.")
            receiver_socket.sendto(b'NACK', sender_address)

if __name__ == "__main__":
    receiver()

