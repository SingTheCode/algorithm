import sys

sys.stdin = open("input.txt")

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # arrCol = [0] * 100
    # arrRow = [0] * 100
    # arrCross1 = 0
    # arrCross2 = 0
    #
    # for i in range(100):
    #     for j in range(100):
    #         arrCol[i] += arr[i][j]
    #         arrRow[j] += arr[i][j]
    #         if i == j:
    #             arrCross1 += arr[i][i]
    #         if i + j == 100:
    #             arrCross2 += arr[i][j]
    #
    # maxCol = arrCol[0]
    # maxRow = arrRow[0]
    #
    # for i in range(100):
    #     if maxCol < arrCol[i]:
    #         maxCol = arrCol[i]
    #     if maxRow < arrRow[i]:
    #         maxRow = arrRow[i]
    #
    # maxValues = [maxCol, maxRow, arrCross1, arrCross2]
    # result = 0
    # for i in range(4):
    #     if result < maxValues[i]:
    #         result = maxValues[i]
    # print(f"#{T} {result}")

    # 교수님 풀이
    c1 = c2 = 0
    for i in range(100):
        c1 += arr[i][i]
        c2 += arr[i][99 - i]
    max_sum = c1 if c1 > c2 else c2

    for j in range(100):
        rs = cs = 0
        for k in range(100):
            rs += arr[j][k]
            cs += arr[k][j]
        if rs > max_sum:
            max_sum = rs
        if cs > max_sum:
            max_sum = cs
    print(f'#{tc} {max_sum}')
