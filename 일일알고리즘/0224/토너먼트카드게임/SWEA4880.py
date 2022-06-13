# 구현
import sys

sys.stdin = open('sample_input.txt')


def f(i, j):
    if i == j:
        return i
    else:
        left = f(i, (i + j) // 2)
        right = f((i + j) // 2 + 1, j)
        return win(left, right)


def win(l, r):
    if arr[l] == 1:
        if arr[r] == 1:
            return l
        if arr[r] == 2:
            return r
        if arr[r] == 3:
            return l
    if arr[l] == 2:
        if arr[r] == 1:
            return l
        if arr[r] == 2:
            return l
        if arr[r] == 3:
            return r
    if arr[l] == 3:
        if arr[r] == 1:
            return r
        if arr[r] == 2:
            return l
        if arr[r] == 3:
            return l


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0]
    arr += list(map(int, input().split()))
    print(f'#{tc} {f(1, N)}')
