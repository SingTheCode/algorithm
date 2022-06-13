import sys

sys.stdin = open('sample_input.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def DFS(si, sj, direct, cnt):
    global visited

    if si == N - 1 and sj == N - 1:
        return

    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if k == direct:
            continue
        if 0 <= ni < N and 0 <= nj < N:
            if arr[si][sj] < arr[ni][nj]:
                if visited[ni][nj] < visited[si][sj] + 2:
                    return
                visited[ni][nj] = visited[si][sj] + 2
            else:
                if visited[ni][nj] < visited[si][sj] + 1:
                    return
                visited[ni][nj] = visited[si][sj] + 1
            DFS(ni, nj, k, )


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cnt = 0
    visited = [[0] * N for _ in range(N)]

    DFS(0, 0, 0)

    print(f'#{tc} {visited[N - 1][N - 1]}')
