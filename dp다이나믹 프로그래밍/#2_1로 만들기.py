# 못풂
# 반복적인 연산(동일한 연산 계속 나옴)> 탑다운 방식으로도 짜보기 

# DP 3단계(보텀업)
x = int(input())

d =[0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i%2 == 0:
        d[i] = min( d[i], d[i//2]+1 )
    if i%3 == 0:
        d[i] = min( d[i], d[i//3]+1 )
    if i%5 == 0:
        d[i] = min( d[i], d[i//5]+1 )
    
print(d[x])