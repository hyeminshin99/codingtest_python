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

# greedy가 쓰일수 있는 이유:
# 2이상의 수(K)로 나누는것이, 1을 빼는것 보다, "항상" N숫자를 빠르게 줄인다.
# 따라서 "당장 나누기(좋은것)를 할수 있다면 한다"/그게 아니라면 나눌수있을때까지 빼자.