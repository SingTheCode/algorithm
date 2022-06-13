import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    maxValue = 0
    maxIndex = 0
    counts = [0] * 10

    for i in range(N):
        counts[arr[i]] += 1

    for i, v in enumerate(counts):
        if maxValue > v:
            continue
        maxValue = v
        maxIndex = i

    print(f"#{tc} {maxIndex} {maxValue}")
