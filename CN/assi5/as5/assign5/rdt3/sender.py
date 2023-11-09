import socket
import hashlib
import random

def sender(msg = "testdata"):
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)  # Change to the receiver's address and port


    expected_seq_num = 0
    while msg:
        message = msg[:4]
        packet_data = message.encode()
        checksum = hashlib.md5(packet_data).digest()
        seq_num = expected_seq_num


        if random.random() > 0.2:
            packet = (1 - seq_num, packet_data, checksum)
        else:
            packet = (seq_num, packet_data, checksum)


        sender_socket.sendto(str(packet).encode(), receiver_address)

        try:
            sender_socket.settimeout(2)  # Timeout for acknowledgments
            response, _ = sender_socket.recvfrom(1024)

            if response == b'ACK'+str(seq_num).encode():
                print(f"Received ACK for packet with seq_num {seq_num}. Moving forward.")
                expected_seq_num = 1 - expected_seq_num
                msg = msg[4:]
            else:
                print(f"Received redundant ACK for packet with seq_num {seq_num}. Resending the packet.")

        except socket.timeout:
            # Timeout, retransmit the packets in the window
            print("Timeout, retransmitting...")

if __name__ == "__main__":

    msg = "Hello, RDT 2.1!"
    sender(msg)

