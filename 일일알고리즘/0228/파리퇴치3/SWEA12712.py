# 팔방탐색
import sys

sys.stdin = open('input.txt')

T = int(input())

di = [-1, 0, 1, 0, 1, 1, -1, -1]
dj = [0, 1, 0, -1, -1, 1, 1, -1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for k in range(4):  # k 방향
                for z in range(1, M):  # 중심에서의 거리
                    ni, nj = i + di[k] * z, j + dj[k] * z
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if maxV < s:  # 최댓값과 비교
                maxV = s

            # X 방향으로 뿌리는 경우
            s = arr[i][j]
            for k in range(4):  # k 방향
                for z in range(1, M):  # 중심에서의 거리
                    ni, nj = i + di[k + 4] * z, j + dj[k + 4] * z
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if maxV < s:  # 최댓값과 비교
                maxV = s
    print(f'#{tc} {maxV}')
