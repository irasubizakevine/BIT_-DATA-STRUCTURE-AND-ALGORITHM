from collections import deque

# Create a queue of 6 patients
chuk_queue = deque(["Patient1", "Patient2", "Patient3", "Patient4", "Patient5", "Patient6"])

# Serve 3 patients (FIFO)
for _ in range(3):
    served = chuk_queue.popleft()
    print(f"Served: {served}")

# Show who's now in front
print("Now in front of CHUK queue:", chuk_queue[0])