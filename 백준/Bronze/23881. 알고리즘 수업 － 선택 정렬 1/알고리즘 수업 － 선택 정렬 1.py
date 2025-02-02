import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

n = len(lst)
cnt = 0
answer = False
for i in range(n-1, 0, -1):
    max_idx = i
    for j in range(0, i):
        if (lst[j] > lst[max_idx]):
            max_idx = j
    lst[i], lst[max_idx] = lst[max_idx], lst[i]
    if not (i == max_idx):
        cnt += 1
    if cnt == K:
        print(lst[max_idx], lst[i])
        exit()

print(-1)