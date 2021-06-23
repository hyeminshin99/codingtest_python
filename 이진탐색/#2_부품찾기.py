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