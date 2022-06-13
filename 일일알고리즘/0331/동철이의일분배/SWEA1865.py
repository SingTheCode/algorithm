# 순열
import sys

sys.stdin = open('input.txt')


def solution(subsets):
    global mmax

    for i in range(len(subsets)):
        ssum = 1
        for j in range(N):
            ssum *= arr[j][subsets[i][j]] / 100
        if ssum > mmax:
            mmax = ssum


def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i] + arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = []
    mmax = 0

    for i in range(N):
        tmp.append(i)

    subsets = permutation(tmp, N)
    solution(subsets)
    print(f'#{tc} {round(mmax * 100, 7)}')
