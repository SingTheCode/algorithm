T = int(input()) # 테스트케이스 개수
for tc in range(1, T+1):
    N = int(input()) # 문제에서의 N
    arr = [list(map(int, input().split())) for _ in range(N)] # 입력받은 행렬이 N인 2차원 배열
    maxSection = 0 # 각 구간의 합 중 최댓값
    tmpSection = 0 # 문제에서 주어진 각 원소의 (1), (2)의 경우에서 구간에 포함된 원소의 합

    for i in range(0, N):
        for j in range(0, N):
            # 원소를 중심으로 한 3 * 3 배열의 구간에 포함된 원소의 합
            if i - 1 >= 0 and i + 1 < N and j - 1 >= 0 and j + 1 < N: # 원소를 중심으로 3 * 3 배열이 arr 배열 안에 포함되어 있는지 확인
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        tmpSection += arr[k][l] # 원소를 중심으로 만든 3 * 3 배열의 원소를 각각 더함
            if maxSection < tmpSection: # 각 구간의 합 중 최댓값이 지금 만든 구간의 합보다 작을 경우
                maxSection = tmpSection # 지금 만든 구간의 합을 각 구간의 합 중 최댓값으로 결정
            tmpSection = 0 # 지금 만든 구간의 합 초기화

            # arr[i][j]부터 한 방향에 arr[i][j]개 씩, 4방향의 구간에 포함된 원소의 합
            for a in range(i - arr[i][j] + 1, i + arr[i][j]): # 4방향 중 세로 줄의 합(상, 하)
                if 0 <= a < N: # 구간이 배열의 범위에 포함될 경우
                    tmpSection += arr[a][j]
            for b in range(j - arr[i][j] + 1, j + arr[i][j]): # 4방향 중 가로 줄의 합(좌, 우)
                if 0 <= b < N: # 구간이 배열의 범위에 포함될 경우
                    tmpSection += arr[i][b]
            tmpSection -= arr[i][j] # 상하, 좌우를 계산하던 중, arr[i][j]의 값이 두번 더해졌으므로 한번 빼줌
            if maxSection < tmpSection: # 각 구간의 합 중 최댓값이 지금 만든 구간의 합보다 작을 경우
                maxSection = tmpSection # 지금 만든 구간의 합을 각 구간의 합 중 최댓값으로 결정
            tmpSection = 0 # 지금 만든 구간의 합 초기화
    print(f'#{tc} {maxSection}')