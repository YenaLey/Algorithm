import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

Deque = deque()

for _ in range(N):
    order = input().split()
    type = order[0]
    if type == "push_front":
        Deque.appendleft(order[1])
    elif type == "push_back":
        Deque.append(order[1])
    elif type == "pop_front":
        if len(Deque):
            print(Deque.popleft())
        else:
            print(-1)
    elif type == "pop_back":
        if len(Deque):
            print(Deque.pop())
        else:
            print(-1)
    elif type == "size":
        print(len(Deque))
    elif type == "empty":
        if not len(Deque):
            print(1)
        else:
            print(0)
    elif type == "front":
        if len(Deque):
            print(Deque[0])
        else:
            print(-1)
    elif type == "back":
        if len(Deque):
            print(Deque[-1])
        else:
            print(-1)