# 🌟다익스트라-우선순위
# 틀림-다시하기

import sys
import heapq

N,M,C = map(int,input().split())
city =[[] for _ in range(N+1)]
distance = [1001]*(N+1)
for _ in range(M):
    X,Y,Z = map(int, sys.stdin.readline().split())
    city[X].append( (Z,Y) ) #거리, 갈도시

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: continue #저장된게 최소면 그대로. 바뀌지x
        for i in city[now]: #들어온 거리가 더 짧으면->연결된 도시들확인
            cost = dist+i[0] #연결된도시까지의 거리 i[0]

        if cost < distance[i[1]]: #거쳐서가는게 더 짧으면 바꾸기
            distance[i[1]] = cost
            heapq.heappush(q,(cost, i[1])) #최단거리 바뀐도시 q에 넣기

dijkstra(C)

count = 0
max_dist = 0
for d in distance:
    if d != 1001 and d!= 0: #INF와 시작노드는 제외
        count += 1
        max_dist = max(d, max_dist)

print(count, max_dist)
