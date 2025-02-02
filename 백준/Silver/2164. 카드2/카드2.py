from collections import deque
import sys

N = int(sys.stdin.readline())

deq = deque([i+1 for i in range(N)])

while(len(deq) != 1):
    deq.popleft()
    deq.append(deq.popleft())

print(deq.pop())