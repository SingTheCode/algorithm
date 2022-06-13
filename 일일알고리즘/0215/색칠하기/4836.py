import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    red_arr = [[0]*10 for _ in range(10)]
    blue_arr = [[0]*10 for _ in range(10)]
    result = 0

    for n in range(N):
        temp_arr = list(map(int, input().split()))
        if temp_arr[4] == 1:
            for i in range(temp_arr[0], temp_arr[2] + 1):
                for j in range(temp_arr[1], temp_arr[3] + 1):
                    if red_arr[i][j] == 0:
                        red_arr[i][j] = 1
        if temp_arr[4] == 2:
            for i in range(temp_arr[0], temp_arr[2] + 1):
                for j in range(temp_arr[1], temp_arr[3] + 1):
                    if blue_arr[i][j] == 0:
                        blue_arr[i][j] = 1
    for i in range(10):
        for j in range(10):
            if red_arr[i][j] == blue_arr[i][j] == 1:
                result += 1
    print(f'#{tc} {result}')

