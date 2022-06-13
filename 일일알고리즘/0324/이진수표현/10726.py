import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = ''
    cnt = 0

    binary = bin(M)
    if len(binary) < 4:
        result = 'OFF'
    else:
        for i in range(len(binary) - 1, len(binary) - N - 1, -1):
            if binary[i] == '1':
                cnt += 1
        if cnt == N:
            result = 'ON'
        else:
            result = 'OFF'

    print(f'#{tc} {result}')
