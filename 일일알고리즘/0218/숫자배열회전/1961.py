import sys
sys.stdin = open("input.txt")

def lotation(beforeChange, size):
    afterChange = [[0] * N for _ in range(N)]
    for i in range(size):
        for j in range(size):
            afterChange[i][j] = beforeChange[j][size - i - 1]
    return afterChange

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    firstLotation = [[0] * N for _ in range(N)]
    secondLotation = [[0] * N for _ in range(N)]
    thirdLotation = [[0] * N for _ in range(N)]

    firstLotation = lotation(arr, N)
    secondLotation = lotation(firstLotation, N)
    thirdLotation = lotation(secondLotation, N)

    print(f'#{tc}')
    for first, second, third in zip(firstLotation, secondLotation, thirdLotation):
        print(f'{"".join(map(str, first))} {"".join(map(str, second))} {"".join(map(str,third))}')