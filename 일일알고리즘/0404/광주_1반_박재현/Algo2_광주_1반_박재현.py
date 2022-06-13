di = [-1, 0, 1, 0]  # 4방향 정의
dj = [0, 1, 0, -1]


def DFS(si, sj, cnt, distance):
    global min_distance  # 최소경로

    if distance > min_distance:  # 현재 경로가 최소 경로보다 클 경우 백트래킹
        return

    if arr[si][sj] == 3:  # 도착 지점 확인
        if min_distance > distance:
            min_distance = distance
        return

    for k in range(4):
        ni = si + di[k]  # 4방향 탐색
        nj = sj + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:  # 0인 경우 distance + 1
                DFS(ni, nj, cnt, distance + 1)
            else:
                if cnt > 0:  # 0이 아니면서 cnt가 0 이상인 경우 벽을 뚫고 이동
                    DFS(ni, nj, cnt - 1, distance + 1)
                else:  # 0이 아니면서 cnt도 0인 경우 멈춤
                    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = -1
    min_distance = 64  # 경로 최솟값 초기화
    print(arr)

    for i in range(N):
        if arr[0][i] == 2:  # 출발지점 찾기
            DFS(0, i, 2, 0)
            break

    if min_distance != 16:
        result = min_distance

    print(f'#{tc} {result}')
