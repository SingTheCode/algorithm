# 퀵정렬
import sys

sys.stdin = open('sample_input.txt')


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    lesser_array, equal_array, greater_array = [], [], []
    for num in array:
        if num < pivot:
            lesser_array.append(num)
        elif num > pivot:
            greater_array.append(num)
        else:
            equal_array.append(num)
    return quick_sort(lesser_array) + equal_array + quick_sort(greater_array)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    sorted_quick = quick_sort(arr)
    print(f'#{tc} {sorted_quick[len(sorted_quick) // 2]}')
