# N개 원소, 최대 K번 교체. A/B그룹. A모든 합 최대되도록

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: break

print(sum(A))