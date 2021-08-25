# G개 탑승구 / P개 비행기 / P개 줄에 각 비행기가 도킹할 탑승구번호 X (1~X까지 도킹가능) / 도킹할수 있는 최대개수?
#🌟아이디어: 매번 비행기를 최적화되게 옮길순 없다. 그렇다고 순서를 바꾸는(sort)것도 안된다.
#           주어진 숫자부터 1까지 전부 확인하려면..? 1~3은 1~4에 포함되어있음. 도킹되있는 갯수만 보면 됨-> 한 집합인가?

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

G = int(input())
P = int(input())

gate = [0]*(G+1) #0번 탑승구는 맨 마지막 판별
for i in range(1, G+1): gate[i] = i

count = 0

plane = list(input() for _ in range(P)) #공간 낭비없이 바로
plane = map(int, plane)

for p in plane:
    root = find_parent(gate, p) #root = find_parent(gate, int(input()))
    if root == 0: break
    union_parent(gate, root, root-1)
    count += 1

print("count: ", count)