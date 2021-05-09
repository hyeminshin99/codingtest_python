# 2021-05-08
# 4번
import sys
input = sys.stdin.readline
INF = int(1e9)

import heapq

V, E = map(int, input().split())
K = int(input()) #시작정점번호

distance = [INF]*(V+1)
gragh = [[] for i in range(V+1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  gragh[u].append((v, w))

def dijkstra(K):
  q=[]
  heapq.heappush(q, (0, K))
  distance[K] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for tu in gragh[now]:
      cost = dist + tu[1]
      if cost < distance[tu[0]]:
        distance[tu[0]] = cost
        heapq.heappush(q, (cost, tu[0]))

dijkstra(K)

for i in range(1, V+1):
  print("INF" if distance[i]==INF else distance[i])
