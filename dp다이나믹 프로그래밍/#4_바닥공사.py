# ๐
# ํ์ผ์ฑ์ฐ๊ธฐ ๋ฌธ์ 
# ์ค์ ์์ด๋์ด! (์์ ๋ชจ๋ ์ค๋ณต์ด๋ฏ๋ก,) ๋งจ ๋ง์ง๋ง์ ์ด๋ป๊ฒ ๋ ์ง ์๊ฐํ๋ค ==> ์ ํ์
# ์ฃผ์! ๋งจ ๋ง์ง๋ง์ "๊ฒฐ๊ณผ๋ฅผ ์ด๋ค ์๋ก ๋๋ ๊ฒฐ๊ณผ ์ถ๋ ฅ" ์์ง๋ง๊ธฐ!

# ์ ํ์ ์ธ์ฐ๊ณ  ๋๋, ํผ๋ณด๋์น์ ๋๊ฐ..!
# ๋ณดํ์ ๋ฐฉ์

N = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, N+1):
    d[i] = (d[i-1] + d[i-2]*2) % 796796  # ๊ฒฐ๊ณผ ๋๋ฌด ์ปค์ง๋ฏ๋ก ๋ฐ๋ก ๋๋๊ฒ ์ ์ฅ

print(d[N])