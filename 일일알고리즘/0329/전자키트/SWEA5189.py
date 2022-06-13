import sys

sys.stdin = open('sample_input.txt')


def solution(si, sj):
    global result
    ssum = 0

    for k in range(N):
        ni = si + k
        nj = sj + k
        if ni >= N:
            ni -= N
        if nj >= N:
            nj -= N
        ssum += arr[ni][nj]

    if ssum < result:
        result = ssum


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1000

    for i in range(1, N):
        solution(0, i)

    print(f'#{tc} {result}')
# 교수님 풀이
# from itertools import permutations
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     pos = [i for i in range(1, N)]
#     answer = 9929292929
#     for p in permutations(pos):
#         tmp = arr[0][p[0]] + arr[p[-1]][0]
#         for j in range(1, N-1):
#             tmp += arr[p[j-1]][p[j]]
#         answer = min(answer, tmp)
#     print(f'#{tc} {answer}')