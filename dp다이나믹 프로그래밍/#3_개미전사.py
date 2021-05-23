# 🌟
# 아이디어 : 아이디어는 뒤에서부터 생각한다-점화식 세우는 방법 / 보텀업방식은 아래서부터 차례로

N = int(input())
array = list(map(int, input().split()))

d = [0]*100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, N):
    d[i] = max( d[i-1], d[i-2]+array[i] )

print(d[N-1])
