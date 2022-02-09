'''
- 문제 해결을 위한 아이디어(Bottom-Up Dynamic Programming)를 Greedy 알고리즘으로 잘못 떠올렸고,
    답안 예시를 참고해 Dynamic Programming 알고리즘으로 재구현했다.
- 문제를 보고 Dynamic Programming 유형임을 파악할 수 있도록
    같은 유형의 문제들을 반복 학습해야겠다.
'''


import time
start_time = time.time()

d = [0] * 30001

X = int(input())



end_time = time.time()
print("time : ", end_time - start_time)