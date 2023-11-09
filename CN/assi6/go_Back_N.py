import random

def transmission(totalFrames, windowSize):
    tt = 0
    i = 1

    while i <= totalFrames:
        z = 0

        for k in range(i, min(i + windowSize, totalFrames + 1)):
            print(f"Sending Frame {k}...")
            tt += 1

        for k in range(i, min(i + windowSize, totalFrames + 1)):
            f = random.randint(0, 1)
            if not f:
                print(f"Acknowledgment for Frame {k}...")
                z += 1
            else:
                print(f"Timeout!! Frame Number: {k} Not Received")
                print("Retransmitting Window...")
                break

        print()
        i += z

    return tt

if __name__ == "__main__":
    totalFrames = int(input("Enter the Total number of frames: "))
    windowSize = int(input("Enter the Window Size: "))
    
    tt = transmission(totalFrames, windowSize)
    
    print(f"Total number of frames which were sent and resent are: {tt}, {tt - totalFrames}")
