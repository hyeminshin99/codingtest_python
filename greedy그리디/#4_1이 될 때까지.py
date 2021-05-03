# N이 1이 될때까지 2가지 과정 중 하나를 수행
# 1. N에서 1 뺀다 / 2. N을 K로 나눈다

N, K = map(int, input().split())
count = 0
while N != 1:
  if(N % K == 0):
    N = N//K
  else:
    N = N-1
  count += 1
print(count)