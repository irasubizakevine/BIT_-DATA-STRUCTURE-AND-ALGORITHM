from collections import deque

# Create a queue of 5 clients
airtel_queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5"])

# Serve two clients
first_served = airtel_queue.popleft()
second_served = airtel_queue.popleft()

print("First served at Airtel:", first_served)
print("Second served at Airtel:", second_served)
