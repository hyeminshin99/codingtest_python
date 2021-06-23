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