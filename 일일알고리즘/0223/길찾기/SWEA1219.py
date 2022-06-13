# 스택, 길찾기
import sys

sys.stdin = open('input.txt')


# 1번 풀이
def dfs(v):
    global visited
    stack = [v]
    while stack:
        v = stack.pop()
        if v == 99:
            return 1
            continue
        if not visited[v]:
            visited[v] = 1
            for j in range(V):
                if G[v][j] == 1 and not visited[j]:
                    stack += [j]
    return 0


T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    V = 100

    visited = [0] * V
    G = [[0] * V for _ in range(V)]
    for i in range(E):
        G[temp[i * 2]][temp[i * 2 + 1]] = 1

    print(f'#{tc} {dfs(0)}')


    # 2번 풀이
    # def dfs(v, destination):
    #     global result
    #     stack = [v]
    #     while stack:
    #         v = stack.pop()
    #         if not visited[v]:
    #             visited[v] = 1
    #             if destination == v:
    #                 result = 1
    #                 break
    #             for j in range(100):
    #                 if G[v][j] and not visited[j]:
    #                     stack.append(j)
    #
    #
    # for _ in range(10):
    #     result = 0
    #     tc, E = map(int, input().split())
    #     arr = list(map(int, input().split()))
    #     G = [[0] * 100 for _ in range(100)]
    #     visited = [0] * 100
    #
    #     for i in range(E):
    #         G[arr[i * 2]][arr[i * 2 + 1]] = 1
    #
    #     dfs(0, 99)
    #     print(f'#{tc} {result}')

    # 교수님 풀이

    # 문제에서 제시한 예시대로 해결
    def DFS(V):
        global result
        visited[V] = 1
        if V == 99:  # 99번 정점을 방문한 상황
            result = 1  # 전역 변수인 result를 1로 변경
            return

        for i in range(100):
            if visited[i] == 0 and (graph[0][V] == i or graph[1][
                V] == i):  # 아직 방문하지 않았고, graph 배열에 포함된 2개의 배열의 인접정점 번호 중에 i와 일치하는 값이 있는 경우
                DFS(i)  # i를 인자로 하는 DFS함수 재귀호출


    for tc in range(1, 11):
        tc, E = map(int, input().split())
        lst = list(map(int, input().split()))

        graph = [[None] * 100 for _ in range(2)]  # 크기가 100인 정적 배열 2개 초기화
        visited = [0] * 100  # 방문표시할 리스트
        # graph = [[1, None,,,,], [2, None,,,,]]

        for i in range(0, len(lst), 2):
            if graph[0][lst[i]] == None:  # 첫번째 배열의 lst[i]번 인덱스에 해당하는 값이 아직 None 인 경우
                graph[0][lst[i]] = lst[i + 1]  # 첫번째 배열에 lst[i+1] 값을 입력
            else:  # 첫번째 배열의 lst[i]번 인덱스에 해당하는 값이 이미 할당된 경우
                graph[1][lst[i]] = lst[i + 1]  # 두번째 배열에 lst[i+1] 값을 입력

        result = 0
        DFS(0)
        print(f'#{tc} {result}')


    # 인접리스트로 해결
    def DFS():
        stack = [0]
        while stack:  # stack이 비어있을때까지 반복
            v = stack.pop()  # stack에 있는 마지막 항목을 꺼냄
            if not visited[v]:  # 해당 정점을 방문하지 않았으면, (이미 방문했으면 아무 동작도 하지 않음)
                visited[v] = 1  # 방문 처리
                stack += graph[v]  # stack 배열에 graph의 v번 배열을 확장
        return visited[99]  # stack이 비어서 반복문을 나오면(탐색을 마쳤을때) 99번 인덱스에 해당하는 값을 반환


    for tc in range(1, 11):
        tc, E = map(int, input().split())
        lst = list(map(int, input().split()))

        graph = [[] for _ in range(100)]  # 최대로 가능한 100개의 인접리스트 초기화
        visited = [0] * 100  # 방문표시할 리스트

        for i in range(0, len(lst), 2):
            graph[lst[i]].append(lst[i + 1])  # 인접 리스트 graph의 lst[i]번 리스트에 lst[i+1]만을 append(방향성이 있으므로 반대로는 하지 않음)

        # print(graph)
        print(f'#{tc} {DFS()}')
