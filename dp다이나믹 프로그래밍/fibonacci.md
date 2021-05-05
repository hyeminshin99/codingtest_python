# DP 접근단계 예시

##   1단계 : 재귀함수
```python
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1) + fibo(x-2) # 재귀
```
print(fibo(4))
***
##   2단계 : 탑다운, 메모이제이션
```python
d = [0] * 100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]                 #메모이제이션
    d[x] = fibo(x-1) + fibo(x-2)   # 재귀-탑다운
    return d[x]
```
print(fibo(99))
***
##   3단계 : 보텀업
```python
d = [0] * 100

d[1] = 1
d[2] = 1
# n = 받고

for i in range(3, n+1):    # 보텀업 (단순 반복문)
    d[i] = d[i-1] + d[i-2]
```
print(d[n])