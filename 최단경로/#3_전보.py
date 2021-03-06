# ๐๋ค์ต์คํธ๋ผ-์ฐ์ ์์
''' ์ ๊ทผ1)'๋ชจ๋ '๋์๋ค ์ต๋จ๊ฑฐ๋ฆฌ์ด๋ฏ๋ก ํ-์๋ผ๊ณ  ์๊ฐํ ์๋ ์๊ฒ ์ง๋ง, N๊ฐฏ์๊ฐ ๋ง์ผ๋ฏ๋กx.  
๋ค๋ฅธ ๋์๊น์ง์ ์ต๋จ๊ฑฐ๋ฆฌ๋ก ๋ด์ distance๋ฆฌ์คํธ์ ๋ฃ์ด๋์ผ๋ฉด ๋ง์ง๋ง์ ๋น๊ตํด์ max๊ฑฐ๋ฆฌ์ธ ๋์๋ฅผ ์ฐพ์ผ๋ฉด ๋จ.  
2)N,M๋ฒ์๊ฐ ๋ง๊ฐ ์ด์->heapq

'''
import sys
import heapq

N,M,C = map(int,input().split())
city =[[] for _ in range(N+1)]
distance = [1001]*(N+1)
for _ in range(M):
    X,Y,Z = map(int, sys.stdin.readline().split())
    city[X].append( (Z, Y) )  #๊ฑฐ๋ฆฌ, ๊ฐ๋์

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: continue #์ ์ฅ๋๊ฒ ์ต์๋ฉด ๊ทธ๋๋ก. ๋ฐ๋์งx
        for i in city[now]: #๋ค์ด์จ ๊ฑฐ๋ฆฌ๊ฐ ๋ ์งง์ผ๋ฉด->์ฐ๊ฒฐ๋ ๋์๋คํ์ธ #i:(๊ฑฐ๋ผ,๊ฐ๋์)
            cost = dist+i[0] #๋ณ์์ ์ธcost:์ฐ๊ฒฐ๋๋์๊น์ง์ ๊ฑฐ๋ฆฌ i[0]
            if cost < distance[i[1]]: #๊ฑฐ์ณ์๊ฐ๋๊ฒ ๋ ์งง์ผ๋ฉด ๋ฐ๊พธ๊ธฐ
                distance[i[1]] = cost
                heapq.heappush(q,(cost, i[1])) #์ต๋จ๊ฑฐ๋ฆฌ ๋ฐ๋๋์ q์ ๋ฃ๊ธฐ

        
dijkstra(C)

count = 0
max_dist = 0
for d in distance:
    if d != 1001 and d!= 0: #INF์ ์์๋ธ๋๋ ์ ์ธ
        count += 1
        max_dist = max(d, max_dist)

print(count, max_dist)
