# 🌟
# N개 떡, 최소 M길이 떡 필요. N개 떡 각각 길이 주어짐. H길이 절단기로 잘라나온 떡들의총합이 M길이이상 되야함. H의 최댓값?

'''import sys

N, M = map(int, input().split())
nlist = list(map(int, sys.stdin.readline().split()))

H = max(nlist)
arr = [0]*len(nlist)

def cut(x, H):
    if x-H < 0: return 0
    return x-H


while sum(arr) >= M:
    arr = list(map(cut(lambda x:x,H), nlist))
    H -= 1

print(H)
'''

'''
파라메트릭 서치 : 최적화문제를->결정문제(예/아니오로 답하는문제)로 바꾸어 해결하는 기법
"원하는 조건을 만족하는 가장 알맞은 값 찾아라 ex.범위내에서 조건을 만족하는 가장 큰 값 찾아라"
=> 보통 이진탐색으로 해결
'''

import sys

N, M = map(int, input().split())
nlist = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(nlist)

H=0

while start <= end:
    sum=0
    mid = (start+end)//2
    for n in nlist:
        if n > mid: sum += n-mid #자르고 남은게 있을때만 더하면 됨
    
    if sum < M: #자른것들합이 M보다작으면, 더많이 잘라야됨
        end = mid-1
    else:       #자른것들합이 M보다크면, 덜 잘라야됨
        H = mid #떡모두합한게 M보다 크거나 같아야 하니까
        start = mid+1

print(H)