# 그리디
import sys

sys.stdin = open('sample_input.txt')


def solution(list1, list2):
    global result

    list1.sort(reverse=True)
    list2.sort(reverse=True)

    win1_index = 10
    win2_index = 10

    for i in range(2, 6):
        if list1[i - 2] == list1[i - 1] == list[i] or list1[i - 2] - 2 == list1[i - 1] - 1 == list1[i]:
            result = 1
            win1_index = i
            break

    for j in range(2, 6):
        if list2[j - 2] == list2[j - 1] == list[i] or list2[j - 2] - 2 == list2[j - 1] - 1 == list2[j]:
            result = 2
            win2_index = j
            break

    if win1_index == win2_index:
        result = 0
    else:
        if win1_index < win2_index:
            result = 1
        else:
            result = 2


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    result = 0

    for i in range(0, 12, 2):
        arr1.append(arr[i])
        arr2.append(arr[i + 1])

    solution(arr1, arr2)

    print(f'#{tc} {result}')
