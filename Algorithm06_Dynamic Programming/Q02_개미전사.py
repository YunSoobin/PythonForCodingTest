'''
- 문제 해결을 위한 아이디어를 떠올리는 데에 어려움이 있어
    해설을 참조하여 학습한 후 다시 풀어 보았다.
- N번째 식량 창고를 선택하는 경우와 (N - 1)번째 식량 창고를 선택하는 경우를 비교한다.
'''


import time
start_time = time.time()

N = int(input())
food = list(map(int, input().split()))

d = [0] * 101
d[1] = food[0]
d[2] = max(food[0], food[1])

for i in range(3, N + 1):
    d[i] = max(d[i - 2] + food[i - 1], d[i - 1])

print(d[N])

end_time = time.time()
print("time  : ", end_time - start_time)