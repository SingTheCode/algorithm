import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    A_len = len(A)
    B_len = len(B)
    count = 0

    i = 0
    while i < A_len - B_len + 1:
        if A[i:i+B_len] == B:
            count += 1
            i += B_len
        else:
            i += 1

    result = A_len - count * B_len + count
    print(f'#{tc} {result}')