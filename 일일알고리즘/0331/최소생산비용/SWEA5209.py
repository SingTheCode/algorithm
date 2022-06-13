# 순열 백트래킹
import itertools
import sys

sys.stdin = open('sample_input.txt')


def solution(subsets):
    global min_sum

    for i in range(len(subsets)):
        ssum = 0
        for j in range(N):
            ssum += arr[j][subsets[i][j]]
            if ssum > min_sum:
                break
        if ssum < min_sum:
            min_sum = ssum


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = []
    min_sum = 100 * 15

    for i in range(N):
        tmp.append(i)

    subsets = list(itertools.permutations(tmp, N))
    solution(subsets)
    print(f'#{tc} {min_sum}')
