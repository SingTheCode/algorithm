import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    result = ""
    keys = ['ZRO', "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    counts = [0] * 10
    TC, N = list(input().split())
    N = int(N)
    arr = list(input().split())
    dic = {}
    for i in range(N):
        if arr[i] == "ZRO":
            counts[0] += 1
        if arr[i] == "ONE":
            counts[1] += 1
        if arr[i] == "TWO":
            counts[2] += 1
        if arr[i] == "THR":
            counts[3] += 1
        if arr[i] == "FOR":
            counts[4] += 1
        if arr[i] == "FIV":
            counts[5] += 1
        if arr[i] == "SIX":
            counts[6] += 1
        if arr[i] == "SVN":
            counts[7] += 1
        if arr[i] == "EGT":
            counts[8] += 1
        if arr[i] == "NIN":
            counts[9] += 1
    for j in range(10):
        for k in range(counts[j]):
            result += keys[j] + " "
    print(f'{TC} {result}')

    # ## 교수님 풀이
    # counting_dict = {}
    # for num in arr:
    #     try:
    #         counting_dict[num] += 1
    #     except:
    #         counting_dict = 1
    # for i in keys:
    #     for j in range(counting_dict[i]):
    #         print(tc, end=" ")
    #     print()