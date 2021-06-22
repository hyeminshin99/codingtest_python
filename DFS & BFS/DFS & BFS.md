# DFS / BFS - "그래프 탐색"을 위한 대표적인 두 알고리즘
***
#### Stack
> append() pop()
#### Queue
> deque() : append() popleft()
```python
from collections import deque
Q = deque()
Q.append(5)
Q.popleft()
list(Q) #리스트로 변경가능
```
#### 재귀함수
> 컴구조적으로 함수호출순서가 stack과 동일
- 꼭 if문으로 종료조건 구현해주어야 함. 
***
## DFS(깊이우선탐색) - stack-재귀함수
> 가장 먼 노드까지 감
```python
# graph:인덱스번호노드에 따라 연결되있는 노드번호 : [ [],[1노드에 연결된 노드들], [2노드에 연결된 노드들], ... ]
# v:현재노드 / visited:방문유무
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]: ##v노드에 연결되있는 노드들
        if not visited[i]:
            dfs(graph, i, visited) #재귀

visited = [False]*N
dfs(graph, 1, visited)
```
## BFS(넒이우선탐색) - queue-큐자료구조deque()
> 가장 가까운 노드먼저 
```python
from collections import deque #큐사용(리스트)

def bfs(graph, start, visited):
    Q = deque([start])
    visited[start] = True

    while Q: #Q에 아무것도 없을때까지
        v = Q.popleft() #노드뽑기pop
        print(v, end=' ')

        for i in graph[v]: ##v노드에 연결되있는 노드들
            if not visited[i]:
                Q.append(i) #노드넣기push
                visited[i] = True

visited = [False]*N
bfs(graph, 1, visited)
```