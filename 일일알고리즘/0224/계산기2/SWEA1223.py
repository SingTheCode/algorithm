# 스택
import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    quest = input()
    numberStack = []
    operatorStack = []

    for char in quest:
        if char == '+':
            operatorStack.append('+')
        elif char == '*':
            operatorStack.append('*')
        else:
            try:
                if operatorStack[-1] == '*':
                    operatorStack.pop()
                    tmp = numberStack.pop()
                    numberStack.append(tmp * int(char))
                else:
                    numberStack.append(int(char))
            except:
                numberStack.append(int(char))

    for _ in range(len(operatorStack)):
        try:
            b = numberStack.pop()
            a = numberStack.pop()
            numberStack.append(a + b)
        except:
            print('error')
            break
    print(f'#{tc} {numberStack.pop()}')
