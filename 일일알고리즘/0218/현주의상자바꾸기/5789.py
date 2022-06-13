import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * (N + 1)

    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L, R + 1):
            arr[i] = q
    print(f'#{tc}', *arr[1:])