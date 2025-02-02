import sys
input = sys.stdin.readline

N = input()
lstN = input().split()

M = input()
lstM = input().split()

cntDict = dict()

for card in lstN:
    if card in cntDict:
        cntDict[card] += 1
    else:
        cntDict[card] = 1

for hisCard in lstM:
    if hisCard in cntDict:
        print(cntDict[hisCard], end = ' ')
    else:
        print(0, end = ' ')