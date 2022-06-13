# 최소 신장 트리
import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    arr.sort(key=lambda x: x[2])  # 가중치로 간선 정렬 (정점1, 정점2, 가중치)
    mst = []
    p = [0]  # 상호배타적 집합

    for i in range(1, V + 1):
        p.append(i)  # 각 정점 자신이 집합의 대표


    def find(u):
        if u != p[u]:
            p[u] = find(p[u])  # 경로압축
        return p[u]


    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1  # 임의로 root2가 root1의 부모


    tree_edges = 0  # 간선 개수
    mst_cost = 0  # 가중치 합

    while True:
        if tree_edges == V:
            break
        u, v, wt = arr.pop(0)
        if find(u) != find(v):  # u와 v가 서로 다른 집합에 속해 있으면
            union(u, v)
            mst.append([u, v])
            mst_cost += wt
            tree_edges += 1

    print(f'#{tc} {mst_cost}')
