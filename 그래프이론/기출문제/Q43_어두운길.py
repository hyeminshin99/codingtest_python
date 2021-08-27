# N개집 0~N-1 / M개도로 / X집에서 Y집사이 Z비용도로 // 모두 이어지되, 절약할 수 있는 최대 금액
# 크루스칼

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

N, M = map(int, input().split())
parent = [0]*N
for i in range(N):
    parent[i] = i

edges = []
result = 0

for _ in range(M):
    X, Y, Z = map(int, input().split())
    edges.append((Z, X, Y))
edges.sort()

for e in edges:
    Z, X, Y = e
    if find_parent(parent, X) != find_parent(parent, Y):
        union_parent(parent, X, Y)
    else:
        result += Z

print(result)