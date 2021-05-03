# greedy
N, M = map(int, input().split())
arr = [[int(x) for x in input().split()] for y in range(N)] #2차원배열한번에받기 @외
marr=[]

for data in arr:
  marr.append(min(data))
print(max(marr))