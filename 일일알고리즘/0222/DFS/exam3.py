# DFS
import sys

sys.stdin = open('input.txt')


def dfs(v):
    global visited
    stack = [v]
    # stack이 비어있을 때까지
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(f'방문 정점: {v}, 방문 체크: {visited}')
            for j in range(1, V + 1):
                if G[v][j] == 1 and not visited[j]:
                    stack.append(j)
        print(stack)


V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0] * (V + 1) for _ in range(V + 1)]
visited = [0] * (V + 1)

for i in range(0, E):
    G[temp[i * 2]][temp[i * 2 + 1]] = 1
    G[temp[i * 2 + 1]][temp[i * 2]] = 1
print(G)

dfs(1)
