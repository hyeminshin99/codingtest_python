# N개 여행지, M개 여행계획에 속한 도시수 / N*N행렬: 1연결,0연결x - 양방향 / 맨마지막줄 M개 계획여행지 번호
#🌟 아이디어: 여행 계획에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능..!

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

# graph = [[] for _ in range(N)] 필요없음..
parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

data = []
for i in range(N):
    data.append(list(map(int, input().split())))  #미리 받아놓으면 그만큼 공간필요하므로 낭비--읽기만 하려면, 아래에서 하면됨

for i in range(0, N): #원래는 1~N인데, 0~N-1로 하고 맨 마지막에 번호바꾸기!
    #data = list(map(int, input().split())) #읽기만 하기!
    for j in range(0, i):
        if data[i][j] == 1:
            union_parent(parent, i+1, j+1)
#            graph[i].append(j)
#            graph[j].append(i)

M_list  = list(map(int, input().split()))

result =True

for i in range(M-1): # 0~M-2 인덱스까지
    if find_parent(parent, M_list[i]) != find_parent(parent, M_list[i+1]):
        result = False

print("YES" if result else "NO")