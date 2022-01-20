'''
- 문제 해결을 위한 아이디어는 쉽게 떠올릴 수 있었다.
- 문제 해결 이후 리스트 자료형의 활용에 부족함을 느껴
    파이썬 문법에 대하여 추가 학습했다.
'''

import time
start_time = time.time()

N, M = map(int, input().split())
num_list = []
max_num = 0

for i in range(N):
    num_list.append(list(map(int, input().split())))

for i in range(N):
    max_num = max(min(num_list[i]), max_num)

print(max_num)

end_time = time.time()
print("time : ", end_time - start_time)