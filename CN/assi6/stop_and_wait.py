import random
import time

def sender_send(data):
    print(f"Sender sent: {data}")
    return data

def sender_receive_ack(expected_sequence_number):
    received_ack = random.randint(0, 1)
    if received_ack:
        print("Sender received ACK")
    else:
        print("Sender did not receive ACK")

def sender_stop_and_wait(data):
    sender_send(data)
    while True:
        sender_receive_ack(0)  # Expected sequence number is 0 in Stop-and-Wait
        if random.random() < 0.2:
            print("Timeout, retransmitting...")
            sender_send(data)
        else:
            break

# Test the Stop-and-Wait protocol
message = "Frame 0"

while message:
    sender_stop_and_wait(message)
    message = input("Enter the next message (or leave empty to end): ")

def receiver_receive(data):
    received_data = data
    print(f"Receiver received: {received_data}")
    return received_data

def receiver_send_ack():
    return random.randint(0, 1)

def receiver_stop_and_wait(data):
    received_data = receiver_receive(data)
    ack = receiver_send_ack()
    while ack == 0:
        print("Receiver received a corrupted frame. Requesting retransmission...")
        ack = receiver_send_ack()
    return ack

# Test the Stop-and-Wait protocol at the receiver side
message = "Frame 0"

while message:
    ack = receiver_stop_and_wait(message)
    if ack:
        message = input("Enter the next message (or leave empty to end): ")
