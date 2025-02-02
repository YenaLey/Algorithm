from collections import deque

n, k = map(int, input().split())

lst = [i for i in range(1,n+1)]
queue = deque(lst)

if n<k:
    k = k % n

lst2 = []

while(len(queue)!=0):
    count = 1
    while(1):
        pop_data = queue.popleft()
        if count == k:
            break
        queue.append(pop_data)
        count += 1
    lst2.append(str(pop_data))

print('<', end='')
print(', '.join(lst2), end='')
print('>')