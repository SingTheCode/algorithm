# 스택
import sys

sys.stdin = open('sample_input.txt')

T = int(input())
operators = ['*', '/', '-', '+', '.']
for tc in range(1, T + 1):
    stack = []  # 숫자 넣는 stack
    result = None
    arr = input().split()
    for text in arr:
        if text == '.':
            if len(stack) > 1:  # stack에 3개 이상 존재할 경우
                result = 'error'
                break
            result = stack.pop()
            break
        elif not text in operators:  # 숫자 들어오면 무조건 push
            stack.append(text)
        else:
            # 인호님 풀이
            # try:                      # stack에 2개 이상 남지 않았을 경우
            #     b = stack.pop()       # try except로 예외 처리
            #     a = stack.pop()
            # except:
            #     result = 'error'
            #     break
            if len(stack) < 2:  # stack에 2개 이상 남지 않았을 경우
                result = 'error'
                break
            a = int(stack.pop())
            b = int(stack.pop())
            if text == '+':
                stack.append(b + a)
            if text == '-':
                stack.append(b - a)
            if text == '*':
                stack.append(b * a)
            if text == '/':
                stack.append(b // a)

    print(f'#{tc} {result}')
