import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    maxFall = 0

# 최대 100층에서부터의 반복
    for i in range(100, 0, -1):
        cnt = 0
        start = 101
        # 맨 아래부터 위로 올라가면서 i랑 같은 층 탐색
        for j in range(N, 0, -1):
            # 같은 층인 개수 구하고 가장 높은 층 인덱스 가져오기
            if boxes[j-1] == i:
                boxes[j-1] -= 1
                cnt += 1
                start = j-1
        # i랑 같은 층이 존재하면
        if cnt > 0:
            fall = (N - start) - cnt
            if maxFall < fall:
                maxFall = fall

    print(f'#{tc} {maxFall}')