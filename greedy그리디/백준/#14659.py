# 산봉우리 높이 주어짐. 왼->오 순서대로 가면서 자기보다 낮은산은 물리칠수있고, 높은산만나면 죽음. 처치할수 있는 최대 숫자?

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


# 하나씩 보면서, 계속 max로 가장 좋은 거 선택. / 또한 더 높은 산 있으면 count 0으로 시작해서 현재가장큰거랑 비교.
N = int(input())
arr = list(map(int, input().split()))
ans = 0
count = 0
max_h = 0

for now in arr:
  if now > max_h:
    count = 0
    max_h = now
  else:
    count += 1
  ans = max(ans, count)
print(ans)