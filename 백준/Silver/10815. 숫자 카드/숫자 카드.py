import sys

N = int(input())
lstN = sorted(list(map(int, sys.stdin.readline().split()))) #오름차순 정렬

M = int(input())
lstM = list(map(int, sys.stdin.readline().split()))

#이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for k in lstM:
    if binary_search(lstN, k, 0, N-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')