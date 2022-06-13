T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for i in range(N - K + 1):  # K * K 그물이 들어갈 수 있는 모든 경우 탐색
        for j in range(N - K + 1):
            ssum = 0  # 물고기의 합
            for p in range(j + 1, j + K):  # 각각의 시작점에서의 K * K 그물망에서 테두리 부분만 탐색
                ssum += arr[i][p]
                ssum += arr[i + K - 1][p - 1]
            for q in range(i, i + K - 1):
                ssum += arr[q][j]
                ssum += arr[q + 1][j + K - 1]
            if max_sum < ssum:  # 현재 물고기의 최댓값이 가장 큰 경우 max_sum을 현재 물고기의 합으로 최신화
                max_sum = ssum

    print(f'#{tc} {max_sum}')
