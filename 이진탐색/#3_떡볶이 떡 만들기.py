# ๐
# N๊ฐ ๋ก, ์ต์ M๊ธธ์ด ๋ก ํ์. N๊ฐ ๋ก ๊ฐ๊ฐ ๊ธธ์ด ์ฃผ์ด์ง. H๊ธธ์ด ์ ๋จ๊ธฐ๋ก ์๋ผ๋์จ ๋ก๋ค์์ดํฉ์ด M๊ธธ์ด์ด์ ๋์ผํจ. H์ ์ต๋๊ฐ?

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
ํ๋ผ๋ฉํธ๋ฆญ ์์น : ์ต์ ํ๋ฌธ์ ๋ฅผ->๊ฒฐ์ ๋ฌธ์ (์/์๋์ค๋ก ๋ตํ๋๋ฌธ์ )๋ก ๋ฐ๊พธ์ด ํด๊ฒฐํ๋ ๊ธฐ๋ฒ
"์ํ๋ ์กฐ๊ฑด์ ๋ง์กฑํ๋ ๊ฐ์ฅ ์๋ง์ ๊ฐ ์ฐพ์๋ผ ex.๋ฒ์๋ด์์ ์กฐ๊ฑด์ ๋ง์กฑํ๋ ๊ฐ์ฅ ํฐ ๊ฐ ์ฐพ์๋ผ"
=> ๋ณดํต ์ด์งํ์์ผ๋ก ํด๊ฒฐ
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
        if n > mid: sum += n-mid #์๋ฅด๊ณ  ๋จ์๊ฒ ์์๋๋ง ๋ํ๋ฉด ๋จ
    
    if sum < M: #์๋ฅธ๊ฒ๋คํฉ์ด M๋ณด๋ค์์ผ๋ฉด, ๋๋ง์ด ์๋ผ์ผ๋จ
        end = mid-1
    else:       #์๋ฅธ๊ฒ๋คํฉ์ด M๋ณด๋คํฌ๋ฉด, ๋ ์๋ผ์ผ๋จ
        H = mid #๋ก๋ชจ๋ํฉํ๊ฒ M๋ณด๋ค ํฌ๊ฑฐ๋ ๊ฐ์์ผ ํ๋๊น
        start = mid+1

print(H)