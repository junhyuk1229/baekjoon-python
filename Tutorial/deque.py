#Dont know why but faster than list

from collections import deque

a = deque([])
a.append(1)
a.appendleft(-1)
a.pop()
a.popleft()