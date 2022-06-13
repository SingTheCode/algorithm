import sys
from functools import reduce

sys.stdin = open("input.txt")

# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#
#     maxNum = reduce(lambda a, b: a if a > b else b, arr)
#     minNum = reduce(lambda a, b: a if a < b else b, arr)
#
#
#     while True:
#         minIndex = []
#         maxIndex = []
#
#         for i in range(100):
#             if maxNum == arr[i]:
#                 maxIndex.append(i)
#             if minNum == arr[i]:
#                 minIndex.append(i)
#         if not len(maxIndex) > 0:
#             maxNum -= 1
#             continue
#         if not len(minIndex) > 0:
#             minNum += 1
#             continue
#         maxFloor = arr[maxIndex[len(maxIndex)-1]]
#         minFloor = arr[minIndex[len(minIndex)-1]]
#
#         minLength = len(maxIndex) if len(maxIndex) <= len(minIndex) else len(minIndex)
#         if cnt + minLength > N or maxNum == minNum:
#             result = maxFloor - minFloor
#             break
#         if len(maxIndex) > len(minIndex):
#             for j in range(minLength):
#                 arr[maxIndex[j]] -= 1
#                 arr[minIndex[j]] += 1
#                 cnt += 1
#             minNum += 1
#             continue
#
#         if len(maxIndex) < len(minIndex):
#             for j in range(minLength):
#                 arr[maxIndex[j]] -= 1
#                 arr[minIndex[j]] += 1
#                 cnt += 1
#             maxNum -= 1
#             continue
#         else:
#             for j in range(minLength):
#                 arr[maxIndex[j]] -= 1
#                 arr[minIndex[j]] += 1
#                 cnt += 1
#             maxNum -= 1
#             minNum += 1
#             continue
#
#     print(f"#{tc} {result}")

# 교수님 풀이
for tc in range(1, 11):
    dump_times = int(input())
    boxes = list(map(int, input().split()))
    # 높이의 값에 해당하는 index를 1씩 더해준다.
    heights = [0] * 101             # 박스 높이의 분포를 카운팅하기 위한 초기화
    max_height = 0
    min_height = 100
    for box in boxes:
        heights[box] += 1
        if max_height < box:
            max_height = box
        if min_height > box:
            min_height = box
    for dump in range(dump_times):
        if max_height - min_height < 2:
            break
        heights[max_height] -= 1
        heights[max_height - 1] += 1
        heights[min_height] -= 1
        heights[min_height + 1] += 1

        if heights[max_height] == 0:
            max_height -= 1
        if heights[min_height] == 0:
            min_height += 1

        result = max_height - min_height
    print(f'#{tc} {result}')

