'''
- 문제 해결을 위한 아이디어를 떠올리는 데에 어려움이 있어
    해설을 참조하여 학습한 후 다시 풀어 보았다.
- 바닥을 앞에서부터 채운다고 가정하면,
    마지막 바닥을 (1 * 2) 2개, (2 * 1) 2개, (2 * 2) 1개 중 어느 것으로 채울지만 정하고
    Memozation 기법을 사용하여 남은 크기를 채울 수 있는 경우의 수를 가져온다.
'''


import time
start_time = time.time()

N = int(input())

d = [0] * 1001
d[1] = 1    # N = 1, (2 * 1) 1개
d[2] = 3    # N = 2, (2 * 1) 2개, (1 * 2) 2개, (2 * 2) 1개

for i in range(3, N + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[N])

end_time = time.time()
print("time : ", end_time - start_time)