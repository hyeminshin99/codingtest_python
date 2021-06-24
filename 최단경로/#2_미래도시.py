#🌟플로이드-워셜
# 1-> K -> X 가는 최단경로. 모든 거리1.

INF = int(1e9)

N, M = map(int, input().split())
company = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    company[i][i]=0
for _ in range(M):
    a,b = map(int, input().split())
    company[a][b] = 1
    company[b][a] = 1 #양방향이동가능
X, K = map(int, input().split())

for i in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            company[a][b] = min(company[a][b], company[a][i]+company[i][b])

distance = company[1][K] + company[K][X]
print(-1 if distance>=INF else distance) #INF보다 크거나 같을때