# G개 탑승구 / P개 비행기 / P개 줄에 각 비행기가 도킹할 탑승구번호 X (1~X까지 도킹가능) / 도킹할수 있는 최대개수?

G = int(input())
P = int(input())

gate = [0]*(G+1) #0번 탑승구는 안씀
plane = list(input() for _ in range(P))
plane = map(int, plane)
count = 0
tmp = False

# plane.sort() 하면안됨..

for p in plane:
    for i in range(p, 1, -1):
        if gate[i] == 0:
            gate[i] = p
            count += 1
            tmp = True
            break
    if tmp == False: break
    else: tmp = False

print("count: ", count)

    
