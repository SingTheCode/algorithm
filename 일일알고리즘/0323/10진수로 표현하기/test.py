# 비트연산
# 학생풀이
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):

    bite = input()
    print(bite)

    for i in range(6, len(bite), 7):
        result = 0

        for j in range(7):
            if bite[i - j] == '1':
                result += 1 << j
        print(result, end=" ")
    print()
