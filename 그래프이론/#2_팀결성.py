# N이하 양의정수, M번 연산. 
# 0 a b : a팀+b팀 합치기 / 1 a b : a,b같은팀?->출력YES/NO

N, M = map(int, input().split())
x, a, b = map(int, input().split())

if x == 0:
    a+b

elif x == 1:
    print("YES" if a==b else "NO")