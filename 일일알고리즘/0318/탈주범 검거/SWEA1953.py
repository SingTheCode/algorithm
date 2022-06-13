# BFS
# 교수님 풀이
import sys

sys.stdin = open('sample_input.txt')

pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)
opp = [1, 0, 3, 2]  # current 위치의 방향에 상응하는 방향 베열


def BFS(N, M, si, sj, L):
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)

        if v[ci][cj] == L:
            return cnt

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            # 현재 위치의 파이프 방향과 다음 위치의 상응하는 파이프 방향이 존재할 경우
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and \
                    pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1  # 경과된 시간 += 1
                cnt += 1
    return cnt


# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = BFS(N, M, R, C, L)
    print(f'#{test_case} {ans}')
