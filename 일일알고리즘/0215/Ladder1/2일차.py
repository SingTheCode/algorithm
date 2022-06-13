import sys
sys.stdin = open("input.txt")

def move(x, y, direction, arr):
    if direction == 0:
        if y+1 <= 99 and arr[x][y+1] == 1:
            return move(x, y+1, 1, arr)
        if y - 1 >= 0 and arr[x][y - 1] == 1:
            return move(x, y - 1, -1, arr)
        if x-1 >= 0 and arr[x-1][y] == 1:
            return move(x-1, y, 0, arr)
        if x == 0:
            return y
    if direction == 1:
        if x-1 >= 0 and arr[x-1][y] == 1:
            return move(x-1, y, 0, arr)
        if y+1 <= 99 and arr[x][y+1] == 1:
            return move(x, y+1, 1, arr)
    if direction == -1:
        if x-1 >= 0 and arr[x-1][y] == 1:
            return move(x-1, y, 0, arr)
        if y - 1 >= 0 and arr[x][y - 1] == 1:
            return move(x, y - 1, -1, arr)







for T in range(10):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    # for i in range(100):
    #     if matrix[99][i] == 2:
    #         print(f'#{tc} {move(99, i, 0, matrix)}')
    #         break



    ### 교수님 풀이
    r = 99
    for i in range(100):
        if matrix[99][i] == 2:      # 도착 지점의 열번호 찾기
            c = i
            break

    d = [-1, 1]                     # 현재 위치의 좌우 만을 확인하기 위한 델타 배열

    while r > 0:
        for i in range(2):
            nc = c + d[i]           # 내 좌우를 보기 위해 임시로 만든 변수
            if 0 <= nc < 100 and matrix[r][nc]: # 사다리 판을 벗어나지 않으면서 좌우 길 존재 여부 확인
                matrix[r][c] = 0    # 이동 전 위치에 해당하는 값을 0으로 변경
                c = nc              # 이동
                break
            else:
                r -= 1
    print(f'#{tc} {c}')