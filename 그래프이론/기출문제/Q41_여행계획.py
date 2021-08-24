# N개 여행지, M개 여행계획에 속한 도시수 / N*N행렬: 1연결,0연결x - 양방향 / 맨마지막줄 M개 계획여행지 번호
#🌟

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
data = []
for i in range(N):
    data.append(list(map(int, input().split())))

for i in range(0, N): #원래는 1~N인데, 0~N-1로 하고 맨 마지막에 번호바꾸기!
    for j in range(0, i):
        if data[i][j] == 1:
            graph[i].append(j)
            graph[j].append(i)

M_list  = map(int, input().split()-1)

now = M_list[0]

def find(n, next):
    if next not in graph[n]:
        for i in graph[n]:
            find(i, next)
    else:
        now = next


find(now, M_list[1])


for i in range(M):
    if M_list[i+1] not in graph[M_list[i]]:
        for m in M_list[i]:
            if graph[m] in 
