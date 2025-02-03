num1 = input()

result = 0
for i in range(1, int(num1)+1):
    num2 = str(i + sum(map(int, str(i))))
    if (num1 == num2):
        result = i
        break

print(result) 