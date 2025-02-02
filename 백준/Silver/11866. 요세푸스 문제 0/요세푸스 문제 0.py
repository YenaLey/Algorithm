from collections import deque

n, k = map(int, input().split())

lst = [i for i in range(1,n+1)]
queue = deque(lst)
lst2 = [] #결과

if n<k:
    k = k % n

while(len(queue)!=0): # n이 0이거나, 모두 pop된 경우 break
    count = 1
    while(1):
        pop_data = queue.popleft()
        if count == k:
            break
        queue.append(pop_data)
        count += 1
    lst2.append(str(pop_data)) #join하기 위해 str로 변환

print('<', end='')
print(', '.join(lst2), end='')
print('>')