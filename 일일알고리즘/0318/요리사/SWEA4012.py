# DFS, 백트래킹
import sys

sys.stdin = open('sample_input.txt')


# 실패
# def solution(array):
#     global minTaste
#     for i in range(N):
#         for j in range(i + 1, N):
#             A = array[i][j] + array[j][i]
#             for k in range(N):
#                 for l in range(k + 1, N):
#                     if i != k and i != l and j != k and j != l:
#                         B = array[k][l] + array[l][k]
#                         if minTaste > abs(A - B):
#                             minTaste = abs(A - B)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     minTaste = 20000
#     solution(arr)
#
#     print(f'#{tc} {minTaste}')

# 교수님 풀이
def DFS(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == len(blst):
            asum = bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            if ans > abs(asum - bsum):
                ans = abs(asum - bsum)
        return

    DFS(n + 1, alst + [n], blst)
    DFS(n + 1, alst, blst + [n])


# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 12345678
    DFS(0, [], [])
    print(f'#{test_case} {ans}')
