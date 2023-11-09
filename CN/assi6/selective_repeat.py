import random

def transmission(totalFrames, windowSize):
    receiveWindow = [0] * (windowSize + 1)
    smallestUnacknowledgedFrame = 0
    tt = 0

    while smallestUnacknowledgedFrame < totalFrames:
        for k in range(smallestUnacknowledgedFrame, min(smallestUnacknowledgedFrame + windowSize, totalFrames)):
            if receiveWindow[k] == 0:
                print(f"Sending Frame {k + 1}...")
                tt += 1

        for k in range(smallestUnacknowledgedFrame, min(smallestUnacknowledgedFrame + windowSize, totalFrames)):
            f = random.randint(0, 1)
            if not f:
                print(f"Acknowledgment for Frame {k + 1}...")
                receiveWindow[k] = 1
            else:
                if receiveWindow[k] == 0:
                    print(f"Timeout!! Frame Number: {k + 1} Not Received")
                    print("Retransmitting Window...")

        print()

        for i in range(smallestUnacknowledgedFrame, min(smallestUnacknowledgedFrame + windowSize + 2, totalFrames)):
            if receiveWindow[i] == 0:
                smallestUnacknowledgedFrame = i
                break

        if receiveWindow[smallestUnacknowledgedFrame] == 1:
            return tt

    return tt

if __name__ == "__main__":
    totalFrames = int(input("Enter the Total number of frames: "))
    windowSize = int(input("Enter the Window Size: "))
    
    tt = transmission(totalFrames, windowSize)
    
    print(f"Total number of frames which were sent and resent are: {tt}, {tt - totalFrames}")
