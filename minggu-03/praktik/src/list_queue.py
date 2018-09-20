from collections import deque
queue = deque(["Eric", "Jhon", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
queue
