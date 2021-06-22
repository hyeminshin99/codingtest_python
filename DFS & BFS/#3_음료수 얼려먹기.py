# 🌟DFS
# N*M크기 얼음틀. 0인부분은 뚫려있어 얼음 얼릴수있음. 총 생성되는 얼음개수?

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

def dfs(x,y):
    if x<0 or y<0 or x>N-1 or y>M-1: #범위조심! 0~N-1 / 0~M-1
        return False

    if graph[x][y] == 0: #물 채울수있으면(아직방문x)
        graph[x][y] = 1 #물넣기

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