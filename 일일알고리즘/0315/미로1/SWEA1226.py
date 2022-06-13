# DFS, BFS
import sys

sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 교수님 풀이 BFS
def BFS(r, c):
    Q = [[r, c]]
    while Q:
        r, c = Q.pop(0)

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 3:
                    return 1
                if not maze[nr][nc]:
                    Q.append([nr, nc])
                    maze[nr][nc] = 1
    return 0


# 교수님 풀이 DFS
# def DFS(r, c):
#     global flag
#
#     if maze[r][c] == 3:
#         flag = 1
#         return
#     maze[r][c] = 1
#     for i in range(4):
#         nr, nc = r + dr[i], c + dc[i]
#         if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
#             DFS(nr, nc)


T = 10
for _ in range(1, T + 1):
    tc = input()
    N = 16

    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
                maze[i][j] = 1

    print(f'#{tc} {BFS(r, c)}')
