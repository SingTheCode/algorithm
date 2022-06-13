# BFS
import sys
from collections import deque

sys.stdin = open('sample_input.txt')

T = int(input())


def bfs(i, j, cnt):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    queue = deque([(i, j)])
    while True:
        (i, j) = queue.popleft()
        if not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 0 and not visited[ni][nj]:
                        queue.append((ni, nj))
                    if arr[ni][nj] == 3:
                        cnt -= 1
                        return cnt
            if not queue:
                return 0


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                startI = i
                startJ = j
                break

    print(f'#{tc}', bfs(startI, startJ, result))
