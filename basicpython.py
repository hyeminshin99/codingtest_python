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
[i if i> 1 else 0 for i in list1]
# 만약 else 가 없다면, if 문은 맨 마지막 위치에 적는다
[i for i in list1 if i>1]