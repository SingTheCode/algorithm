# 스택
import sys

sys.stdin = open('sample_input.txt')
T = int(input())

for tc in range(1, T + 1):
    text = input()
    tl = []
    for i in text:
        if not tl or tl[-1] != i:
            tl.append(i)
        else:
            tl.pop()
    print(f'#{tc} {len(tl)}')
