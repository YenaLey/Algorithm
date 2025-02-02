import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()

for k in lst:
    print(k)