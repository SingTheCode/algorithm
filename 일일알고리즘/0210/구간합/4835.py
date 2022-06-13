import sys
from functools import reduce

sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max = 0
    min = 10000 * M

    for i in range(N-M+1):
        sample = arr[i:i+M]
        temp = reduce(lambda a, b: a + b, sample)
        max = temp if max < temp else max
        min = temp if min > temp else min
    result = max - min

    print(f"#{tc} {result}")