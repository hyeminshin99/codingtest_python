# 선수강강의->수강강의. 여러개 동시에 들을 수 있음. 각 강의에 대하여 수강하기까지 걸리는 최소시간?
# 🌟위상정렬

from collections import deque
import copy

N = int(input())
graph = [[] for i in range(N+1)]
indegree = [0]*(N+1) #진입차수
time = [0]*(N+1)

for i in range(1, N+1):
    line = list(map(int, input().split())) #한줄 입력받아 배열로 저장하는 방식!-기억하자0
    time[i] = line[0]
    for j in line[1:-1]: #인덱스 1~ -2까지. 맨마지막은 항상 -1로 끝남(문제조건)
        indegree[i] += 1
        graph[j].append(i) #주의! j->i 이므로 그래프에 j가 i가리키도록 넣어야함

#위상정렬함수
def topology_sort():
    result = copy.deepcopy(time) #각 강의수강시간 최소 저장. 계속 갱신
    Q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)

    while Q:
        now = Q.popleft()
        for a in graph[now]: #now에 연결되있는 노드들 하나씩
            result[a] = max(result[a], result[now] + time[a]) #갱신
            indegree[a] -= 1

            if indegree[a] == 0:
                Q.append(a)

    for i in range(1, N+1):
        print(result[i])


topology_sort()