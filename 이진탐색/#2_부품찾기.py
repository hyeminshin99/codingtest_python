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