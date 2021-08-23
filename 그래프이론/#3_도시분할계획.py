# 도시 2개로 분할 / 분리된 각 마을의 집들은 연결 / 길의 유지비 최소로
# N집개수, M길개수 
### 접근> 그래프-집합,서로소--최소?경로반드시존재-크루스칼알고리즘-신장트리
# 다 연결하고, 마지막에 제일 큰 경로 삭제!-정답
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

N,M = map(int, input().split())
parent = [0]*(N+1)
for i in range(N):
    parent[i] = i

citys = []
result = [] #마지막에 제일큰 cost 길만 끊기

for i in range(M):
    A, B, C = map(int, input().split()) #C가 cost
    citys.append((C, A, B))
citys.sort()

for city in citys:
    C, A, B = city
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result.append(C)

result.remove(max(result)) #사실 위에서 이미 sort했기때문에, 가장 마지막에 들어온게 최대비용간선임..max(result)==result[-1]
print(sum(result))

# result를 배열로 놓으면 또 공간을 차지하게 되므로, 그냥 변수로 설정하는 법
# result = 0    last = 0 으로해서 last도 계속 갱신. 마지막에 print(result-last)