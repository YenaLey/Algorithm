M = int(input())

ball_position = 1  # 공의 위치 (초기값: 1번 컵)

for _ in range(M):
    X, Y = map(int, input().split())
    if ball_position == X:
        ball_position = Y
    elif ball_position == Y:
        ball_position = X

print(ball_position)
