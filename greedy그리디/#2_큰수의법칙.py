# 주어진 배열의 수들을 M번 더하여, 가장 큰 수 만들기
# 특정 인덱스의 수가 연속해서 K번 초과하여 더해질 수 없다.
# ex) 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5  =  46

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
kcount = 0

data.sort(reverse=True) #data.sort() : 원본바뀜 / sprt(data, ) : 원본안바뀜
while M!=0:
  if kcount < K: # <= 로 해서 틀림
    ans += data[0]
    kcount += 1
  else:
    if data[1]!=data[0]:
      ans += data[1]
    kcount = 0
  M -= 1
    
print(ans)