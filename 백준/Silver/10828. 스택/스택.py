import sys

# n = int(input())
n = int(sys.stdin.readline())

s = []

for _ in range(n):
    # str = input("").split()
    str = sys.stdin.readline().split()
    o = str[0]

    if o == "push":
        s.append(str[1])
    elif o == "pop":
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif o == "size":
        print(len(s))
    elif o == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif o == "top":
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])

