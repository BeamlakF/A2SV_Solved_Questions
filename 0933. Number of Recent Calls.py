from collections import deque

def __init__(self):
        self.queue = deque()
        #intializing an empty queue
        

def ping(self, t: int) -> int:
    self .queue.append(t)
    # Adding the new ping to the back of the queue
    while self. queue [0] < t - 3000:
        self.queue.popleft()
        #to remove the ones at from the window that is t -3000

    return len(self.queue) 
