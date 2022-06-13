T = int(input()) # 테스트케이스 수

for tc in range(1, T + 1):
    N, K = map(int, input().split()) # 각 테스트케이스의 N, K
    arr = [list(map(int, input().split())) for _ in range(N)] # 입력받은 2차원 배열
    maxSection = 0 # 구간합의 최댓값

    for i in range(0, N):
        tmpSection = 0 # 각 행의 구간의 합
        for j in range(i, K + i):
            if j < N: # 열의 인덱스가 N행의 크기를 넘지 않을 때까지만 계산
                tmpSection += arr[i][j] # 해당 구간의 합을 계산
        if maxSection < tmpSection: # 구간합의 최댓값과 지금 계산한 구간의 합이 크다면
            maxSection = tmpSection # 지금 계산한 구간의 합을 구간합의 최댓값으로 함
    print(f'#{tc} {maxSection}')