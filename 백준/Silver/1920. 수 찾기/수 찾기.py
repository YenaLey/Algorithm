import sys

N = int(sys.stdin.readline())
lst1 = set(sys.stdin.readline().split())

M = int(sys.stdin.readline())
lst2 = sys.stdin.readline().split()

for n in lst2:
    if n in lst1:
        print(1)
    else:
        print(0)