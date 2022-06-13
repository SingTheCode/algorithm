import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = s = maxI = 0
    while s < N:
        maxI = s
        for i in range(s, N):
            if arr[maxI] < arr[i]:
                maxI = i
        for i in range(s, maxI):
            result += arr[maxI] - arr[i]
        s = maxI + 1
    print(f'#{tc} {result}')