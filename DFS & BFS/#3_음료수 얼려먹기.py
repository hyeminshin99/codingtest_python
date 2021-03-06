# ๐DFS
# N*Mํฌ๊ธฐ ์ผ์ํ. 0์ธ๋ถ๋ถ์ ๋ซ๋ ค์์ด ์ผ์ ์ผ๋ฆด์์์. ์ด ์์ฑ๋๋ ์ผ์๊ฐ์?

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

def dfs(x,y):
    if x<0 or y<0 or x>N-1 or y>M-1: #๋ฒ์์กฐ์ฌ! 0~N-1 / 0~M-1
        return False

    if graph[x][y] == 0: #๋ฌผ ์ฑ์ธ์์์ผ๋ฉด(์์ง๋ฐฉ๋ฌธx)
        graph[x][y] = 1 #๋ฌผ๋ฃ๊ธฐ

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

    return False


count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1

print(count)