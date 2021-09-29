# 한 강의실에 최대한 많이 강의할수있는 갯수

N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)] #안쪽[a, b]이렇게 들어감. input().split()으로 나눠진수를 하나씩 for문을 통해서 []안에 넣음
arr.sort(key = lambda x:(x[1],x[0])) # x[1]로만 sort하니 오답. sort기준 주의!
count = 0
last = 0

for i in arr:
  s, e = i[0], i[1]
  if s >= last:
    last = e
    count += 1

print(count)