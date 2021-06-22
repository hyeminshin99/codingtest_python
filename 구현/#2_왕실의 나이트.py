# 나이트 처음 시작위치 주어짐. L자로만 이동할 수 있을때, 이동할 수 있는 경우의수

#ord() : 특정문자 아스키코드값으로 변환. ord('a') : 97
start = str(input())
x, y = ord(start[0])-96, int(start[1])
count = 0

moves = [(-2,-1),(-2,1),(2,-1),(2,1), (-1,-2),(-1,2),(1,-2),(1,2)]
for move in moves:
    dx = x+move[0]
    dy = y+move[1]
    if dx<1 or dy<1 or dx>8 or dy>8:
        continue
    count += 1
    #print(move)
print(count)
