import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    numbers = list(input())
    numberStack = []
    operatorStack = []
    result = ""
    numberArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for temp in numbers:
        if temp in numberArr:
            numberStack.append(temp)
        else:
            operatorStack.append(temp)
    # print(numberStack)
    for number in numberStack:
        result += number
    for i in range(len(operatorStack)):
        result += operatorStack.pop()

    print(f'#{tc} {result}')
