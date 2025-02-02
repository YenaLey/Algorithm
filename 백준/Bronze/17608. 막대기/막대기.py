import sys

N = int(sys.stdin.readline())
stack = list()

for _ in range(N):
    stack.append(int(sys.stdin.readline()))

test_length = stack.pop()
cnt = 1

for _ in range(len(stack)):
    top  = stack.pop()
    if  top > test_length:
        cnt += 1
        test_length = top

print(cnt)