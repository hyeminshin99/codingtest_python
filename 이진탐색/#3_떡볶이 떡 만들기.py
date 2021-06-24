# 🌟
# N개 떡, 최소 M길이 떡 필요. N개 떡 각각 길이 주어짐. H길이 절단기로 잘라나온 떡들의총합이 M길이이상 되야함. H의 최댓값?

import sys

N, M = map(int, input().split())
nlist = list(map(int, sys.stdin.readline().split()))

H = 2000000000
arr = [0]*len(nlist)

def cut(x):
    global H
    if x-H < 0: return 0
    return x-H


while sum(arr) >= M:
    arr = list(map(cut, nlist))
    H -= 1

print(H)