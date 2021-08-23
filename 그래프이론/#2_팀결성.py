# 0~N번까지(N+1개)팀, M번 연산. 
# 0 a b : a팀+b팀 합치기 / 1 a b : a,b같은팀?->출력YES/NO
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    #else: 아님!!! 모든 경우에 return
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b: #a가 크거나 같다 나머지모두로해도 되니까 else써도됨
        parent[a] = b


N, M = map(int, input().split())
parent=[0]*(N+1)
for i in range(0, N+1):
    parent[i] = i

for i in range(M):
    x, a, b = map(int, input().split())
    if x == 0:
        union(parent, a, b)

    elif x == 1:
        print("YES" if find_parent(parent,a)==find_parent(parent,b) else "NO")