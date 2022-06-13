# 스택
import sys

sys.stdin = open('sample_input.txt')


def dfs(v, destination):
    global visited
    stack = [v]
    while stack:
        v = stack.pop()
        if v == destination:
            print(f'#{tc} 1')
            return
        if not visited[v]:
            visited[v] = 1
            for j in range(1, V + 1):
                if G[v][j] == 1 and not visited[j]:
                    stack.append(j)
    print(f'#{tc} 0')


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(0, E):
        start, end = map(int, input().split())
        G[start][end] = 1

    startNode, endNode = map(int, input().split())
    dfs(startNode, endNode)
