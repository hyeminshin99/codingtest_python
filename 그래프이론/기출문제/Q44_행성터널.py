# 행성N개 / 각 행성의 x,y,z좌표 / 터널비용은 min(ads(x-x), y-y, z-z) / 모든행성 연결 최소비용
# 크루스칼 #🌟시간초과!!

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
# points = []   #전체 다 받아서 한번에 계산하면 시간초과. x,y,z 따로 비교해서 3번*N하면 최적!
edges = []
result = 0

x = []
y = []
z = []

for i in range(N):
    X, Y, Z = map(int, input().split()) #변수다르게 해야함..!
    x.append((X, i)) #노드의 번호 꼭 같이 저장해놓기!
    y.append((Y, i))
    z.append((Z, i))

x.sort() #이때 sort할때는 절댓값x... 노드끼리의 가까운 정도대로 정렬하기!
y.sort()
z.sort()

for i in range(N-1):
    edges.append((x[i+1][0]-x[i][0], x[i][1],  x[i+1][1] )) #이미 위에서 sort했기 때문에 더큰애-작은애 abs()쓴것처럼 됨-->cost
                                    #x[i][1] : a노드의 번호  /  x[i+1][1] : b노드의 번호
    edges.append((y[i+1][0]-y[i][0], y[i][1],  y[i+1][1] ))
    edges.append((z[i+1][0]-z[i][0], z[i][1],  z[i+1][1] ))
    
edges.sort() #그럼 알아서 abs(x1-x2), abs(y1-y2), abs(z1-z2) 중에 min가장 작은거 들어감..ㄷㄷ..

for e in edges:
    cost, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)