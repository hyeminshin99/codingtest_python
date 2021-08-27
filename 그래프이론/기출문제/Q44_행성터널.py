# 행성N개 / 각 행성의 x,y,z좌표 / 터널비용은 min(ads(x-x), y-y, z-z) / 모든행성 연결 최소비용
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


N = int(input())

parent = [0]*N
for i in range(N):
    parent[i] = i
points = []
edges = []
result = 0

for _ in range(N):
    x,y,z = map(int, input().split())
    points.append((x,y,z))

for i in range(N-1):
    for j in range(i+1, N):
        x1,y1,z1 = points[i]
        x2,y2,z2 = points[j]
        cost = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
        edges.append((cost, i, j))
    
edges.sort()

for e in edges:
    cost, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)