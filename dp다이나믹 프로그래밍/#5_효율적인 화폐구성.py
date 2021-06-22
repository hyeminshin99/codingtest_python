# 🌟일부 별표
# 화폐종류 N개, M원 만드는 최소화폐사용개수. N개 화폐 원 알려줌

N,M = map(int, input().split())
value = [int(input()) for _ in range(N)]

d = [0]*10001

for i in range(1, M+1):  #M+1 +1 안해서 틀림
    #d[i] = d[i-value[0]]+1
    for j in value:
        if j <= M:
            d[i] = min(d[i], d[i-j]+1)

print(-1 if d[M]==0 else d[M])