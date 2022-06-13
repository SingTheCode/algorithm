# 메모이제이션 그리디
import sys

sys.stdin = open('sample_input.txt')

di = [1, 0]
dj = [0, 1]


def DFS(si, sj, ssum):
    global result

    if result <= ssum:
        return

    if si == N - 1 and sj == N - 1:
        if ssum < result:
            result = ssum
        return

    for k in range(2):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            DFS(ni, nj, ssum + arr[ni][nj])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 260
    # result = sum(sum(arr, [])) # 이차원 배열의 요소를 모두 더하는 방법

    DFS(0, 0, arr[0][0])
    print(f'#{tc} {result}')
