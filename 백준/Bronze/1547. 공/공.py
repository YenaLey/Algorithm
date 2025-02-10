M = int(input())

cup = ["1", "0", "0"]
for _ in range(M):
  X, Y = map(int, input().split())
  cup[X-1], cup[Y-1] = cup[Y-1], cup[X-1]

cupStr = ''.join(cup)
print(cupStr.find("1")+1)