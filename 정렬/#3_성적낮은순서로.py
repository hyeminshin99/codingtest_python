# N개 이름 성적 으로 들어오고, 성적 낮은 순서대로 출력
N = int(input())
dic={}
for i in range(N):
    name, score = input().split()
    dic[name]=score

print(dic)

dic=sorted(dic.items(), key = lambda x: x[1]) #list가됨...🌟🌟
#dic.sort(key = dic.values()) #key로 dic.values() 안됨..

print(dic)

for i in dic:
  print(i[0], end =' ')

#print(dic.keys()) #현재 dic는 list. 튜플아니라서 keys못읽음.
