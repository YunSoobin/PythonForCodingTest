'''
- 문제 해결을 위한 아이디어
    ( 나의 답안 : 정렬 알고리즘을 사용하지 않고, Numpy 라이브러리 사용 )
    ( 답안 예시 : 정렬 알고리즘 사용 )
- 배열의 원소를 교체하는 방식은 답안과 일치하게 떠올렸다.
'''


import time
start_time = time.time()

import numpy

N, K = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

for _ in range(K):
    minIndexA = numpy.argmin(arrayA)
    maxIndexB = numpy.argmax(arrayB)

    if arrayA[minIndexA] < arrayB[maxIndexB]:
        arrayA[minIndexA], arrayB[maxIndexB] = arrayB[maxIndexB], arrayA[minIndexA]

print(sum(arrayA))

end_time = time.time()
print("time : ", end_time - start_time)