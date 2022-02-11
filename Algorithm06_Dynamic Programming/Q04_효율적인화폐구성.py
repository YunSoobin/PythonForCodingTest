'''
- 문제 해결을 위한 아이디어를 떠올리는 데에 어려움이 있어
    해설을 참조하여 학습한 후 다시 풀어 보았다.
- 화폐 단위를 k, 가치의 합을 i라 가정하면,
    i원을 만드는 최소 화폐 개수 = (i - k)원을 만드는 최소 화폐 개수 + 1
    위 과정을 모든 k에 적용하여 가장 작은 수를 해당 i의 DP 테이블에 Memozation
'''


import time
start_time = time.time()

N, M = map(int, input().split())

coin = []   # 화폐 종류
for _ in range(N):
    coin.append(int(input()))

d = [10001] * 10001 # 10001은 M원을 만드는 것이 불가능함을 의미
d[0] = 0    # 0원을 만드는 화폐 개수는 0

for k in coin:
    for i in range(k, M + 1):
        d[i] = min(d[i], d[i - k] + 1)

if d[M] == 10001:   # 10001은 M원을 만드는 것이 불가능함을 의미
    print(-1)
else:
    print(d[M])

end_time = time.time()
print("time : ", end_time - start_time)