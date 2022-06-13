# 백트래킹
import sys

sys.stdin = open('sample_input.txt')


def DFS(cur, change):
    global min_change

    # 가지치기2
    if min_change <= change:
        return

    # # 가지치기3
    # if cur + arr[cur] >= N:
    #     if min_change > change + 1:
    #         min_change = change + 1
    #     return

    if cur >= N:
        if min_change > change:
            min_change = change
        return

    for i in range(1, arr[cur] + 1):
        DFS(cur + i, change + 1)


T = int(input())
for tc in range(1, T + 1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    arr = [0]
    arr += tmp[1:]
    min_change = N

    DFS(1, -1)

    print(f'#{tc} {min_change}')
