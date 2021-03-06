# dp 다이나믹 프로그래밍-동적계획법
## "이미 했던 연산이 반복되는 결점을 보완"하기 위해서 만들어냄. 중복 연산 줄이자.
## 처음 진행되는 연산은 기록해 두고, 이미 진행했던 연산이라면 다시 연산하는 것이 아니라 기록되어 있는 값을 가져오는 방식.
#
- 메모리 공간을 좀 더 사용하고, 연산 속도를 증가시킬수있음.
- 모든 방법을 일일이 검토하여 최적의 해를 찾아내는 방식의 알고리즘
#
- <->그리디greedy와 대비됨.(순간마다 그 순간에서의 최적의 해를 찾는 방식)
- 따라서 시간은 오래걸리지만, 항상 최적의 해를 찾아냄.
#
***
## DP로 해결할 수 있는 문제 ex) 피보나치 수열
#
> ### DP 쓸수 있는 조건
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은, 그걸 포함하는 큰 문제에서도 동일하다
***
### 2가지 방법
>- 탑다운 : 큰 문제를 해결하기 위해, 작은 문제를 호출 ===메모이제이션
 - 보텀업 : 작은문제부터 차근차근 답 도출. 단순히 반복문만 이용
 보텀업이 DP 전형적인 형태.
### 메모이제이션 기법
#
***
## 접근단계
> 0. 완전탐색 으로 접근 -> 시간 오래걸림 -> 해결하고자하는 부분 문제들에 중복있음==>DP적용
 1. 일단 단순 "재귀함수"로-비효율적인 프로그램 작성 (탑다운)
 2. 작은 문제에서 구한 답이, 큰 문제에서 그대로 사용될 수 있으면, 코드개선-메모이제이션
 3. "보텀업"방식- 재귀함수x. 단순 "반복문"만 사용
 - ex)fibonacci.md