import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1], [1, 1]]
    tmp =[]
    for i in range(2, N + 1):
        tmp.append(1)
        for j in range(0, i - 1):
            tmp.append(arr[i-1][j] + arr[i-1][j + 1])
        tmp.append(1)
        arr.append(tmp)
        tmp = []

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])

