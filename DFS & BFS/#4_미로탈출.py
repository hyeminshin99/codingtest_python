# 🌟BFS / graph자체에 거리를 저장하도록 했음
# 1부분으로만 움직일수있음. 출발(1,1) ~> 도착(N,M) 움직여야 하는 최소칸의 갯수

from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

#상하좌우
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
            if graph[nx][ny] == 1: #처음방문했을때만
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs(0, 0)
print(graph[N-1][M-1])