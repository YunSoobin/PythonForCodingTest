'''
- 문제 해결을 위한 아이디어와 정답 구현은 답안과 일치하고, 쉽게 떠올릴 수 있었다.
- 아이디어에 대한 근거 설명은 연습이 더 필요할 것 같다.
'''


import time
start_time = time.time()

N, K = map(int, input().split())

# 1. N이 K의 배수가 될 때까지 N에서 1을 뺀다.
count = 0   # 결과값(과정 수행의 최소 횟수)
while N % K != 0:
    N -= 1
    count += 1

# 2. N이 1이 될 때까지 N을 K로 나눈다.
while N != 1:
    N /= K
    count += 1

print(count)

end_time = time.time()
print("time : ", end_time - start_time)