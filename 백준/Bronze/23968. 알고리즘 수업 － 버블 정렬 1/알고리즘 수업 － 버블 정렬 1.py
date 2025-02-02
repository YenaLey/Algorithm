import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(len(lst) - 1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            cnt += 1
            if cnt == K:
                print(lst[j], lst[j+1])
                exit()
        
print(-1)