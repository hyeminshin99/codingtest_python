# dp 접근단계 예시

##   1단계 : 재귀함수
def fibo(x):  
    if x==1 or x==2:  
        return 1  
<u>    return fibo(x-1) + fibo(x-2)</u>
print(fibo(4))  

***
