import socket
import hashlib

def receiver():
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 12345)  # Change to the receiver's address and port

    receiver_socket.bind(receiver_address)

    expected_seq_num = 0

    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        received_packet = eval(data.decode())  # Decode and evaluate the packet

        seq_num, packet_data, checksum = received_packet

        if seq_num == expected_seq_num:
            calculated_checksum = hashlib.md5(packet_data).digest()
            if calculated_checksum == checksum:
                print(f"Received valid message: {packet_data.decode()}")
                receiver_socket.sendto(b'ACK'+str(expected_seq_num).encode(), sender_address)
                expected_seq_num = 1 - expected_seq_num
            else:
                print("Received a corrupt message. Sending NACK.")
                receiver_socket.sendto(b'ACK'+str(1 - expected_seq_num).encode(), sender_address)
        else:
            print(f"Received out-of-sequence packet with seq_num {seq_num}. Sending NACK.")
            receiver_socket.sendto(b'ACK'+str(1 - expected_seq_num).encode(), sender_address)

if __name__ == "__main__":
    receiver()

