import sys
sys.stdin = open("sample_input.txt")
T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    input_arr = list(map(int, input().split()))
    arr = [0] * N
    for m in range(M):
        arr[input_arr[m]] = 1

    i = 0
    result = 0

    while i < N:
        for j in range(K):
            # 목적지에 이미 들어왔으면 반복문 종료
            if i+K-j >= N:
                i = N
                break
            # K만큼 떨어진 곳부터 하나씩 줄여가며 충전소 탐색
            if arr[i+K-j] == 1:
                i = i+K-j
                result += 1
                break
            # 없으면 result = 0 하고 반복문 종료
            if j == K-1:
                result = 0
                i = N
                break

    print(f"#{tc} {result}")