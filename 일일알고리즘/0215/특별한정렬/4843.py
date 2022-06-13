import sys
sys.stdin = open("sample_input.txt")

# def bubblesort(arr):
#     for i in range(len(arr)-1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    result = []

    for i in range(N // 2):
        result.append(arr[N-i-1])
        result.append(arr[i])
    if N % 2 != 0:
        result.append(arr[N // 2 + 1])
    print(f'#{tc} ', end="")
    for j in range(10):
        print(result[j], end=' ')
    print()
