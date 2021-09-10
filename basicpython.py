# vs 여러줄주석 Ctrl+K+C
# 아스키코드
ord('A') #65 #문자를 숫자로
chr(65) #A #숫자를 문자로


# One-line
# if-else : A if 조건 else B if 조건 else C
print('A' if True else 'B')

# 이중for문
[i*j for j in list2 for i in list1]
      # 2번 for 문     # 1번 for문

# for,if-else가 함께 쓰일 경우, if 문을 for문 보다 앞에 적는다
[i if i>1 else 0 for i in list1]
# 만약 else 가 없다면, if 문은 맨 마지막 위치에 적는다
[i for i in list1 if i>1]


# 제곱, 제곱수, 파이
import math

print(5**2) #25
pow(a,b) #a의 b제곱을 계산해서, 반환하는 함수

math.sqrt(4) # 2.0
math.pi #3.1415926535897931


##### 튜플dict - key, value / items() ##########
# 튜플 값 넣기
dic={}
dic['a']=100 #{'a':100}

# key로 value찾기
my = {'a':1, 'b':2}
my['b'] #2 / 없으면 Error  ##dict(a) 가 아니라 dict[a] 임!
my.get('b') #2 / 없으면 None / get(x, '디폴트 값')

my.keys()   # dict_keys(['a', 'b'])
my.values() # dict_values([1, 2])
my.items()  # dict_items([('a', 1), ('b', 2)])

'b' in my #True

# value값으로 key찾기
# 1. dict 뒤집기
my_dict={2:200 , 3:300}
new_dict = dict(map(reversed, my_dict.items()))
print(new_dict) #{200:2 , 300:3}
print(new_dict[300]) #3

# 2. for문 활용
for key, value in my_dict.items():
      if value == 300:
            print(key) #3


##### map함수 (feat.튜플) ##########
# map(func, iter) #func:iter에서 온 값들을 변환하는 함수 / iter에는 list or 튜플 들어감!!
# map은 변환하는 거고, 출력하려면 앞에 출력시킬 타입써줘야됨. list(map(...))

dic = {1:100, 2:200, 3:300}

def func(x):
  return x*2

print(map(func, dic))  #<map object at 0x7f83e41823d0>
print(list(map(func, dic)))  #[2, 4, 6]

# print(dict(map(func, dic))) #오류:key만 넘겨지니까 dict로 변환못함.

print(list(map(func, [dic[i] for i in dic]))) #i로는 key 들어오고, dict[i]가 value임!! #[200, 400, 600]

a=[1,2,3]
a = list(map(lambda i: i-1), a) #a의 모든 원소들 1씩 빼기 ---lambda함수 쓰는법!

#### input받기(feat.map함수) ####
# #기본적으로 원소 str문자열로 받음
A = list(input().split()) #['2', '3', '4', '5']
A = list(map(int, input().split())) #[2, 3, 4, 5]