num1 = int(input())

start = max(1, num1 - 9 * len(str(num1)))  # 탐색 범위를 줄이기
result = 0

for i in range(start, num1):  # 1부터가 아니라 start부터 시작
    if i + sum(map(int, str(i))) == num1:
        result = i
        break

print(result)
