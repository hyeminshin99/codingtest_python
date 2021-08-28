# 작년등수로부터 바뀐 팀들 ( , )쌍으로 주어짐. 올해등수 출력/확실한순위 찾을수없으면 ? / 일관성없으면 IMPOSSIBLE출력
# 위상정렬 #🌟


Testcase = int(input())

for _ in range(Testcase):
    n = int(input()) #팀갯수
    t = list(map(int, input().split())) #작년등수 1~n등 팀번호

    parent = [0]*(n+1)
    for i in range(2, n+1):
        parent[i] = t[i-1]

    m = int(input()) #등수바뀐 쌍
    for _ in range(m):
        a, b = map(int, input().split())

