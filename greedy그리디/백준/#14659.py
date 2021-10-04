# 시간초과.. pypy3으로 하면 되지만, 이중for문이므로 비효율..
N = int(input())
arr = list(map(int, input().split()))
ans = 0

for i in range(N):
  count = 0
  for c in arr[i+1:]:
    if c < arr[i]:
      count += 1
    else:
      break
    ans = max(ans, count)

print(ans)