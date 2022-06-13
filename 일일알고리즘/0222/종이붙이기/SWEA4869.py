# 재귀
import sys

sys.stdin = open('sample_input.txt')

T = int(input())


def combination(n, r):
    if n == r or r == 0:
        return 1
    else:
        return combination(n - 1, r - 1) + combination(n - 1, r)


for tc in range(1, T + 1):
    N = int(input())
    N //= 10
    result = 0

    for i in range(0, N // 2 + 1):
        result += combination(N - i, i) * (2 ** i)

    print(f'#{tc} {result}')

# 교수님 풀이


# for tc in range(1, T + 1):
#     N = int(input())
#     papers = [1, 3]
#
#     for i in range(2, N//10):
#         # f(n) = f(n-2) * 2 + f (n - 1)
#         papers.append(papers[i - 2] * 2 + papers[i - 1])
#         print(f'#{tc} {papers[N//10-1]}')

# p = 1
# for i in range(N//10):
#     if i % 2:
#         p = p * 2 + 1
#     else:
#         p = p * 2 - 1
# print(f'#{tc} {p}')
