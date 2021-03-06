# ๐BFS / graph์์ฒด์ ๊ฑฐ๋ฆฌ๋ฅผ ์ ์ฅํ๋๋ก ํ์
# 1๋ถ๋ถ์ผ๋ก๋ง ์์ง์ผ์์์. ์ถ๋ฐ(1,1) ~> ๋์ฐฉ(N,M) ์์ง์ฌ์ผ ํ๋ ์ต์์นธ์ ๊ฐฏ์

from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

#์ํ์ข์ฐ
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: #์ฒ์๋ฐฉ๋ฌธํ์๋๋ง
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs(0, 0)
print(graph[N-1][M-1])