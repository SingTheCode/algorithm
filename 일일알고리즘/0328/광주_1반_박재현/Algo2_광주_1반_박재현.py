# 상우하좌 방향을 나타낸다
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# DFS로 연결된 길을 전부 탐색한다
def DFS(si, sj):
    global visited, min_ground, max_cnt
    sum_ground = 0  # 탐색한 땅의 가격의 합
    cnt = 0  # 탐색한 땅의 넓이

    if visited[si][sj]:  # 이미 방문했으면 패스(가지치기)
        return

    stack = [(si, sj)]  # stack에 start index 집어넣는다
    while True:
        if not stack:  # stack이 없을 때까지 반복
            if cnt == max_cnt:  # 넓이가 같은 경우, 현재 땅의 값이 기존에 산 땅의 값보다 작은 경우 최신화
                min_ground = min(min_ground, sum_ground)
            if cnt > max_cnt:  # 땅이 더 넓으면, 땅의 가격을 최근에 산 땅들의 가격으로 교체
                max_cnt = cnt
                min_ground = sum_ground
            return
        ci, cj = stack.pop()
        if not visited[ci][cj] and arr[ci][cj]:  # 방문하지 않았고, 구매할 수 있는 땅인 경우
            visited[ci][cj] = 1  # 방문하고
            sum_ground += arr[ci][cj]  # 땅의 가격을 더한다
            cnt += 1

            for k in range(4):  # 인접한 땅 탐색하면서 방문하지 않고, 구매할 수 있는 땅인 경우 stack에 집어넣는다
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj]:
                    stack.append((ni, nj))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]  # 방문 여부 표시
    min_ground = N * N * 5  # 땅의 가격을 전부 합했을 때의 최대값으로 초기화한다
    max_cnt = 0  # 구매하는 땅의 넓이

    for i in range(N):
        for j in range(N):
            DFS(i, j)

    print(f'#{tc} {max_cnt} {min_ground}')
