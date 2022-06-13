import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    sdokuSet = set()
    result = 1
    for i in range(9):
        for j in range(9):
            sdokuSet.add(arr[i][j])
        if len(sdokuSet) < 9:
            result = 0
            break
        sdokuSet.clear()

    for j in range(9):
        for i in range(9):
            sdokuSet.add(arr[i][j])
        if len(sdokuSet) < 9:
            result = 0
            break
        sdokuSet.clear()

    for i in range(0, 9, 3):
        for j in range(i, i+3):
            for k in range(3):
                sdokuSet.add(arr[j][k])
        if len(sdokuSet) < 9:
            result = 0
            break
        sdokuSet.clear()
    print(f'#{tc} {result}')
