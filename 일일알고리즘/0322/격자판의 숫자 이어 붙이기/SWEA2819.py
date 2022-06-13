# DFS
import sys

sys.stdin = open('sample_input.txt')


def DFS(si, sj, stringTmp):
    global resultSet

    if len(stringTmp) == 7:
        resultSet.add(stringTmp)
        return

    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            DFS(ni, nj, stringTmp + arr[si][sj])


T = int(input())

for tc in range(1, T + 1):
    arr = [input().split() for _ in range(4)]

    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]
    resultSet = set()

    for i in range(4):
        for j in range(4):
            DFS(i, j, '')

    print(f'#{tc} {len(resultSet)}')
