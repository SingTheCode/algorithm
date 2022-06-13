# DFS
import sys

sys.stdin = open(' input.txt')


def BFS(v):
    global visited
    global result

    queue = [v]
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            result += str(v)
            for j in range(1, V + 1):
                if G[v][j] == 1 and not visited[j]:
                    queue.append(j)
        if queue:
            result += '-'
    return result


arr = list(map(int, input().split(', ')))
V = 10
G = [[0] * (V + 1) for _ in range(V + 1)]
visited = [0] * (V + 1)
result = ""

for i in range(0, len(arr), 2):
    G[arr[i]][arr[i + 1]] = 1
    G[arr[i + 1]][arr[i]] = 1

print(f'{BFS(1)[:-2]}')
