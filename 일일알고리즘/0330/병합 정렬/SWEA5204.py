# 병합 정렬
import sys

sys.stdin = open('sample_input.txt')


def mergeSort(list):
    size = len(list)
    if size <= 1:
        return list

    mid = len(list) // 2
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])
    merged = merge(left, right)
    return merged


def merge(list1, list2):
    global cnt
    merged = []

    if list1[len(list1) - 1] > list2[len(list2) - 1]:
        cnt += 1
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))

    if len(list1) > 0:
        merged += list1
    if len(list2) > 0:
        merged += list2

    return merged


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    sorted = mergeSort(arr)
    print(f'#{tc} {sorted[len(sorted) // 2]} {cnt}')
