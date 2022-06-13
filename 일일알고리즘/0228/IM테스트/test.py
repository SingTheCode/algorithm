import sys

sys.stdin = open('input.txt')

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                for k in range(0, 4):
                    m = 1
                    while True:
                        ni = i + di[k] * m
                        nj = j + dj[k] * m
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1:
                            arr[ni][nj] = 1
                            m += 1
                        else:
                            break
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    print(f'#{tc} {cnt}')
