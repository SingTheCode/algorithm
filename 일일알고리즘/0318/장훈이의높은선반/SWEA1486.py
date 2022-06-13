# 부분집합
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    minValue = 200000


    # 부분집합 풀이
    # for i in range(1 << N):
    #     array = []
    #     for j in range(N):
    #         if i & (1 << j):
    #             array.append(arr[j])
    #     sumValue = sum(array)
    #
    #     if sumValue >= B:
    #         if minValue >= sumValue:
    #             minValue = sumValue
    #
    # print(f'#{tc} {minValue - B}')

    # DFS 풀이
    def DFS(idx, sumValue):
        global minValue

        if sumValue >= minValue:  # 백트래킹(항상 메모리에 효율적이지는 않음)
            return

        if idx == N:
            if sumValue >= B and minValue > sumValue:
                minValue = sumValue
            return

        DFS(idx + 1, sumValue + arr[idx])
        DFS(idx + 1, sumValue)


    DFS(0, 0)
    print(f'#{tc} {minValue - B}')
