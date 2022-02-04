'''
기본적인 정렬 문제이므로 파이썬 기본 정렬 라이브러리를 사용하여 어렵지 않게 구현할 수 있었다.
'''


import time
start_time = time.time()

N = int(input())
array = [int(input()) for _ in range(N)]
array.sort(reverse=True)

print(array)

end_time = time.time()
print("time : ", end_time - start_time)