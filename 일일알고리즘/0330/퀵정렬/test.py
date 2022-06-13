import sys

sys.stdin = open('input.txt')

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
array3 = list(map(int, input().split()))


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while (left <= right):
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array1, 0, len(array1) - 1)
quick_sort(array2, 0, len(array2) - 1)
quick_sort(array3, 0, len(array3) - 1)

print(array1)
print(array2)
print(array3)
