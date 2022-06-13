# 부분집합
import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    for i in range(1 << 10):
        sumArray = []
        for j in range(10):
            if i & (1 << j):
                sumArray.append(arr[j])
        if len(sumArray) > 0 and sum(sumArray) == 0:
            print(f"#{tc} True")
            break
        if i == 1 << 10 - 1:
            print(f"#{tc} False")
