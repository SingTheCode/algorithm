# 재귀함수
import sys

sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0


def f(p, q, N):
    global white
    global blue
    sum = 0
    for i in range(p, p + N):
        for j in range(q, q + N):
            sum += arr[i][j]
    if sum == 0:
        white += 1
        return
    elif sum == N * N:
        blue += 1
        return
    else:
        f(p, q, N // 2)
        f(p + N // 2, q, N // 2)
        f(p, q + N // 2, N // 2)
        f(p + N // 2, q + N // 2, N // 2)


f(0, 0, N)
print(white)
print(blue)
