'''
- 이진 탐색 학습 직후 해당 문제를 풀어,
    문제 해결을 위한 아이디어로 이진 탐색을 떠올렸다.
- 이진 탐색 구현
    ( 나의 답안 : 재귀 함수 사용 )
    ( 답안 예시 : 반복문 사용 )
- 답안 예시를 참조하여 헷갈리는 파이썬 문법을 추가 학습했다.
'''


import time
start_time = time.time()

def binary_search(array, target, start, end):
    # 종료 조건
    if start > end: # 부품 존재 X
        print("no", end=' ')
        return None

    mid = (start + end) // 2

    if array[mid] == target:    # 부품 존재 O
        print("yes", end=' ')
        return None
    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)
    else:
        binary_search(array, target, mid + 1, end)

N = int(input())
store = list(map(int, input().split()))
store.sort()

M = int(input())
customer = list(map(int, input().split()))

for i in customer:
    result = binary_search(store, i, 0, N - 1)

end_time = time.time()
print("\ntime : ", end_time - start_time)