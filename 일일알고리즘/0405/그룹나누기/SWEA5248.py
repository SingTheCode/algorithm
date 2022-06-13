import sys

sys.stdin = open('sample_input.txt')


def DFS(v):
    global visited
    global result

    stack = []

    if visited[v]:
        return
    stack.append(v)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for k in range(1, N + 1):
                if arr[v][k] == 1 and not visited[k]:
                    stack.append(k)
    result += 1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    result = 0

    for i in range(M):
        arr[tmp[2 * i]][tmp[2 * i + 1]] = 1
        arr[tmp[2 * i + 1]][tmp[2 * i]] = 1

    for j in range(1, N + 1):
        DFS(j)

    print(f'#{tc} {result}')
