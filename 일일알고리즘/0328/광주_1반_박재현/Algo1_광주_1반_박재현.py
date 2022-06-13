# 상하좌우 방향을 나타낸다.
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


# 토끼 위치, 방향, 점프 거리를 받아 방문 표시를 한다.
def solution(si, sj, direct, distance):
    global visited
    ni, nj = si, sj

    while 0 <= ni < N and 0 <= nj < N:  # 토끼가 당근 농장을 벗어날 때까지 로직을 수행한다.
        if visited[ni][nj] == 0:  # 아직 방문 안했으면
            visited[ni][nj] = 1  # 방문
        ni = ni + di[direct] * distance  # 토끼 위치 최신화
        nj = nj + dj[direct] * distance


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0] * N for _ in range(N)]  # 토끼 방문을 나타내는 N * N  배열
    ssum = 0

    for i in range(M):
        solution(arr[i][0], arr[i][1], arr[i][2], arr[i][3])

    for i in range(N):
        for j in range(N):
            ssum += visited[i][j]  # N * N 농장에서 토끼가 방문한 곳을 전부 합한다.
    print(f'#{tc} {ssum}')
