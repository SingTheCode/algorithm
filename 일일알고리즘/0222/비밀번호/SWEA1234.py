# 스택
import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N, numbers = input().split()
    N = int(N)
    stack = []
    top = 0

    for i in range(N):
        if top == 0:
            top += 1
            stack.append(numbers[i])
        else:
            if numbers[i] == stack[top - 1]:
                stack.pop()
                top -= 1
            else:
                stack.append(numbers[i])
                top += 1
    print(f'#{tc}', "".join(stack))
