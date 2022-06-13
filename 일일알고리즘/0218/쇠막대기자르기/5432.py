import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    arr = input()
    result = cnt = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if arr[i-1] == '(':
                result += cnt
            else:
                result += 1
    print(f'#{tc} {result}')