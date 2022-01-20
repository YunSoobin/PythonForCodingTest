'''
- 문제 해결을 위한 아이디어(반복되는 수열에 대해서 파악)는 답안과 일치하게 떠올렸다.
- 시간 복잡도를 낮추기 위해
    구현 과정에서 반복문을 사용하지 않고 계산식으로만 작성하는 방식을 연습해야겠다.
'''


import time
start_time = time.time()

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)

num_sum = 0 # 결과값
group = K + 1   # (가장 큰 값 * K + 두 번째로 큰 값)을 한 group으로 설정

for i in range(K):
    num_sum += num_list[0]
num_sum += num_list[1]

num_sum *= (M // group)

for j in range(M % group):
    num_sum += num_list[0]

print(num_sum)

end_time = time.time()
print("time : ", end_time - start_time)