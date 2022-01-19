import time
start_time = time.time()

N, M, K = list(map(int, input().split()))
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