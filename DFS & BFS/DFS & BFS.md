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
## DFS(깊이우선탐색)