# 부품 N개, 손님이 M개 부품 찾음. 있으면 yes, 없으면 no 출력

#import sys

N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))
ans = ''

for m in mlist:
    if m in nlist: ans+='yes '
    else: ans+='no '

print(ans)


#### 이진탐색-반복문 ####
def BS(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target: return mid
        elif array[mid] > target: end = mid-1
        else: start = mid+1
    return None

N = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
M = int(input())
mlist = list(map(int, input().split()))

for m in mlist:
    result = BS(nlist, m, 0, N-1)
    if result == None:
        print('no', end=' ')
    else: print('yes', end=' ')


#### 계수정렬 ####
N = int(input())
nlist = [0]*1000001
for i in input().split(): #input().split()도 iter !!
    nlist[int(i)] = 1 #일반적으로 input받으면 str임! 잊지말기

M = int(input())
mlist = list(map(int, input().split())) #input().split()이 iter

for m in mlist:
    if nlist[m] >= 1: print('yes ')
    else: print('no ')


#### 집합set()-1개라도 있는지 기록하면되니까 ####
N = int(input())
nlist = set(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

for m in mlist:
    if m in nlist: print('yes ')
    else: print('no ')