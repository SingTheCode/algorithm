import sys
sys.stdin = open("sample_input.txt")

T = int(input())
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(1, T+1):
    result = 0
    N, K = map(int, input().split())
    for i in range(1 << 12):
        sumArray = []
        for j in range(12):
            if i & (1 << j):
                sumArray.append(arr[j])
        if len(sumArray) == N and sum(sumArray) == K:
            result += 1
    print(f'#{tc} {result}')
