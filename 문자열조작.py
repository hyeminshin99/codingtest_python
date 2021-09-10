# .split('기준') : 문자열 분리/ 구분자 문자열 '기준'으로 분리시켜줌 배열로 반환
time_str = "10:34:17"
time_str.split(':') #['10', '34', '17']

#'기준'.join(text) : 연결/ '기준'을 text문자열들을 사이에 넣어 연결
hi = "abcdefg"
print(' '.join(hi)) #a b c d e f g
print('-'.join(hi)) #a-b-c-d-e-f-g

# .strip('문자') : 삭제/ '문자'에 해당되는걸 모두 삭제
#                   //단 좌측 또는 우측에 가장 첫번째로 오는 문자열만 삭제 시도 하기 때문에 중간은 삭제 안될수 있음..
text = "----Hello----World----"
print(text.lstrip('-')) # Hello----World----
print(text.rstrip('-')) # ----Hello----World
print(text.strip('-'))  # Hello----World     >>그럼 replace쓰기..text.replace('-','')

# .replace("a찾을값", "b바꿀값", 바꿀횟수) : 바꾸기/ "문자열"변환. a를 b로 '몇번'바꾸기
text = 'abcabc'
text.replace('a','ke',2) #kebckebc

## .translate(T) : 바꾸기/ "문자"하나씩 변환. T에서 maketrans로 지정한 문자를 특정문자로
text = "Hello, World!"
T = str.maketrans('HWd', '123')
print(text.translate(T)) #1ello, 2orl3!

# .just(길이) .center() : 정렬/ just는 문자를 가운데로 정렬, ljust는 왼쪽으로, rjust는 오른쪽으로
#                                 남는곳은 공백으로 / '길이'가 짧으면 정렬x
text = 'abcdefg' #7개
print(text.ljust(10)) #abcdefg   
print(text.rjust(10)) #   abcdefg
print(text.center(10))# abcdefg  #홀수면앞이작은거로공백
## .zfill('길이') : '길이'만큼 정렬하고, 문자열 앞에는 0채우기
print(text.zfill(10)) #000abcdefg


# .find('찾을값') : 문자열 위치찾기/ 왼쪽에서부터 '찾을값'찾으면 인덱스 반환. 없으면 -1반환
#                                   찾는 문자열의 길이가 2 이상일 경우: 처음 시작하는 문자의 위치인덱스
text = 'Hello, World!'
print(text.find('o'))   #4 #첫번째o 인덱스4
print(text.find('Wor')) #7
print(text.rfind('o'))  #8 #두번째o 인덱스8  ##오른쪽부터 찾음

# .count('찾을값') : '찾을값'문자열 갯수 반환
text = 'Hello, World!'
print(text.count('o'))  #2

# .upper()  .lower()  : 대문자, 소문자로 변환


#--------------------------------------------------#
# filter(함수, iter반복가능한객체) : iter에서 '함수'대로 되서 반환
L = [2, 3, 4, 5, 6, 7, 8, 9]
list( filter(lambda x: x%3==0, L) ) #[3, 6, 9]

def f(x): return x>5
a = [1,2,3,4,5,6,7,8,9]
list ( filter(f,a) ) #[6,7,8,9]

## reduce(함수, iter) : iter에 저장된 요소를 순서대로 '(누적/집계)함수'하여 반환
from functools import reduce #써야함!
a = [1,2,3,4,5]
k = reduce(lambda x,y : x+y ,a) #print(k)-> 15

## punctuation :모든 특수문자 들어가있음.
import string
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

text = '!#$%Hello!:;World./:;'
text.strip(string.punctuation) # Hello!:;World


## .zip : 여러개 iterable 동시에 순회/ 
list1 = [1,2,3,4]
list2 = [100,200,300,400]
list3 = [6,7,8,9]
for i,j,k in zip(list1, list2, list3):
    print(i+j+k)  # 107 209 311 413


## collections.Counter('문자열') : 문자열에 있는 모든 문자 하나당 count몇개
from collections import Counter
print(Counter('hello world'))  #Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

#--------------------------------------------------#
# 정규표현식 re 사용!
# re.sub('패턴', '바꿀문자열/교체함수', 'iter문자열', 바꿀횟수)
import re
re.sub('a|b', 'f', 'abcdaegbb') #a또는b를 f로 바꿔라
re.sub('[0-9]+', 'n', '120 12 F4BF78') #0-9그이상 숫자들 다 찾아서 n으로 바꿔라 #n n FnBFn
re.sub('[0-9]+', lambda i: str(int(i.group()))*2, '120 12 F4BF78') #120120 1212 F44BF7878

re.sub('[^a-z\d\-\_\.]', '', text) #^ 제외하고 지워라
re.sub('^\.|\.$', '', text) #양끝의 . 제거 == text.strip('.')
re.sub('\.\.+', '.', text) #\.\. : .이 2개 이상인거 .한개로 바꿔라
re.sub('aa+', 'a', text) #a가 2개이상이면 a로 바꿔라

re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234') #1234 hello 1234 hello # 그룹 2, 1, 2, 1 순으로


#--------------------------------------------------#
# 리스트 문자열
# list[ 시작값:끝값:step ]

# list.index('찾을값')  :'찾을값'의 인덱스 반환

# list.extend([v1, v2]) :리스트 맨뒤에 값 추가

# list.insert(index, '값') : 'index'위치에 '값'추가

# list.sort(key = ) : key값 기준으로 정렬

# list.reverse() : 값을 역순으로 정렬

