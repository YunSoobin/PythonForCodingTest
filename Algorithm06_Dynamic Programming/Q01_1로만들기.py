'''
- 문제 해결을 위한 아이디어(Bottom-Up Dynamic Programming)를 Greedy 알고리즘으로 떠올렸고,
    답안 예시를 참고해 Dynamic Programming 알고리즘으로 재구현했다.
- 현재 숫자에서 1을 뺀 경우와 (2, 3, 5)로 나눈 경우 중 연산 횟수가 적은 경우을 선택하면 된다.
- 문제를 보고 Dynamic Programming 유형임을 파악할 수 있도록
    같은 유형의 문제들을 반복 학습해야겠다.
'''


import time
start_time = time.time()

X = int(input())

d = [0] * 30001

for i in range(2, X + 1):
    # 1을 빼는 경우
    d[i] = d[i - 1] + 1 # "+ 1"은 1을 빼는 연산 과정을 센 것

    if i % 5 == 0:
        d[i] = min(d[i // 5] + 1, d[i]) # 현재 숫자를 5로 나눈 경우와 1을 뺀 경우 비교
    elif i % 3 == 0:
        d[i] = min(d[i // 3] + 1, d[i]) # 현재 숫자를 3으로 나눈 경우와 1을 뺀 경우 비교
    elif i % 2 == 0:
        d[i] = min(d[i // 2] + 1, d[i]) # 현재 숫자를 2로 나눈 경우와 1을 뺀 경우 비교

print(d[X])

end_time = time.time()
print("time : ", end_time - start_time)