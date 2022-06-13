import sys
from functools import reduce

sys.stdin = open("sample_input.txt")
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_result = min_result = arr[0]

    max_result = reduce(lambda a, b: a if a > b else b, arr)
    min_result = reduce(lambda a, b: a if a < b else b, arr)

    result = max_result - min_result
    print(f'#{tc} {result}')
