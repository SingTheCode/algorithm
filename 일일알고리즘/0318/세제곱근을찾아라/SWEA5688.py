# 완전탐색
import sys

sys.stdin = open('sample_input.txt')


def solution(number):
    i = 0
    while i * i * i <= number:
        if i * i * i == number:
            return i
        i += 1
    return -1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {solution(N)}')
