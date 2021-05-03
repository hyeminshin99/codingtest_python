# 각 행의 가장 낮은 숫자들 중, 가장 큰 숫자 출력

N, M = map(int, input().split())
#arr = [[int(x) for x in input().split()] for y in range(N)] #2차원배열한번에받기 @외
                                                            # 저장공간 낭비
marr=[]

for i in range(N): # 1줄씩 받기(2차원배열저장공간 세이브)
    arr = list(map(int, input().split()))
    marr.append(min(arr)) # append([E,X]):[E,X]추가 / extend([H,M]):E,X 추가

print(max(marr))