# 내림차순으로 정렬
N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort(reverse = True)

for i in arr:
    print(i, end= ' ')