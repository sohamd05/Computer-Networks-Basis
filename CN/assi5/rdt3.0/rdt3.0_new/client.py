import socket
import time

# Function to validate the checksum of a received message
def validate_checksum(message):
    parts = message.split(':')
    received_checksum, received_message, sender_sequence = int(parts[0]), parts[1], parts[2]
    calculated_checksum = 0
    for char in received_message:
        calculated_checksum ^= ord(char)
    
    if calculated_checksum == received_checksum:
        return sender_sequence
    else:
        print(f"Received corrupted message: {received_message}")
        return None

def main():
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = ('localhost', 9799)
    receiver_socket.bind(receiver_address)

    while True:
        data, sender_address = receiver_socket.recvfrom(1024)
        data = data.decode()
        if data.lower() == 'exit':
            break

        sender_sequence = validate_checksum(data)

        if sender_sequence is not None:
            print(f"Received message: {data.split(':')[1]}")
            print(f"Received message from sender sequence: {sender_sequence}")
            receiver_socket.sendto(sender_sequence.encode(), sender_address)
        else:
            print("Received corrupted message. Sending NAK.")
            q = data.split(':')[2]
            if q == '0':
                q = '1'
            else:
                q = '0'
            receiver_socket.sendto(q.encode(), sender_address)

    receiver_socket.close()

if __name__ == "__main__":
    main()
