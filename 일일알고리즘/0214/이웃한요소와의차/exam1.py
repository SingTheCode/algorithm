import sys

sys.stdin = open("input.txt")
T = int(input())
result = 0
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            sumValue = 0
            for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    result += abs(arr[i][j] - arr[ni][nj])

print(result)