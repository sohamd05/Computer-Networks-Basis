import socket
import hashlib
import random
import time

def sender(msg = 'testdata'):
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)  # Change to the receiver's address and port


    while msg:
        message = msg[:4]
        packet = message.encode()
        checksum = hashlib.md5(packet).digest()

        # simulating checksum errors
        if random.random() < 0.2:
            print("Simulating error.")
            checksum = hashlib.md5(packet+'ji'.encode()).digest()

        packet_with_checksum = packet + checksum
        sender_socket.sendto(packet_with_checksum, receiver_address)
        time.sleep(2)

        response, _ = sender_socket.recvfrom(1024)

        if response == b'ACK':
            print("Received ACK. Moving forward.")
            msg = msg[4:]
        else:
            print("Received NACK. Resending the packet.")



if __name__ == "__main__":

    msg = "Hello, RDT 2.0!"
    sender(msg)

