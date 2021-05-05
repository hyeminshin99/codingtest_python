# dp 접근단계 예시

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