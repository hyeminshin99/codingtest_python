# 주어진 배열의 수들을 M번 더하여, 가장 큰 수 만들기
# 특정 인덱스의 수가 연속해서 K번 초과하여 더해질 수 없다.
# ex) 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5  =  46

n, m, k = map(int,input().split())
data = list(map(int,input().split()))
