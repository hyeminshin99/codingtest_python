# N개 이름 성적 으로 들어오고, 성적 낮은 순서대로 출력
N = int(input())
dic={}
for i in range(N):
    name, score = input().split()
    dic[name]=score

dic.sort(key = dic.values())

print(dic.keys())
