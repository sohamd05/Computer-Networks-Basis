import socket
import random

# Function to generate a simple checksum for a message
def generate_checksum(message):
    checksum = 0
    for char in message:
        checksum ^= ord(char)
    return checksum

def main():
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender_socket.settimeout(2)
    receiver_address = ('localhost', 9799)
    
    while True:
        message = input("Enter a message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            sender_socket.sendto(f"{message}".encode(), receiver_address)
            break

        q = random.randint(0, 1)  # Simulate alternating sequence numbers
        prev = q

        for i in range(3):  # Send the same message three times
            # Calculate the checksum of the message
            checksum = generate_checksum(message)

            # Simulate message corruption
            if random.random() < 0.3:
                message = 'new123' + message

            print(message)

            # Send the message with checksum and sequence number
            sender_socket.sendto(f"{checksum}:{message}:{q}".encode(), receiver_address)

            try:
                ack, _ = sender_socket.recvfrom(1024)

                if ack.decode() == str(q):
                    print(f"Message sent successfully: {message}")
                    if q == 0:
                        q = 1
                    else:
                        q = 0
                else:
                    print("NAK received. Retransmitting...")

            except socket.timeout:
                print("Timeout - no response from the receiver.")
                continue

    sender_socket.close()

if __name__ == "__main__":
    main()
