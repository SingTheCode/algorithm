import sys
sys.stdin = open("input.txt")

N = int(input())
maxLen = 0

for i in range(N, N // 2, -1):
    arr = [N]
    arr.append(i)
    idx = 0
    while True:
        tmp = arr[idx] - arr[idx+1]
        if tmp >= 0:
            arr.append(tmp)
            idx += 1
        else:
            if maxLen < len(arr):
                result = arr
                maxLen = len(arr)
            break
print(maxLen)
print(" ".join(map(str, result)))
