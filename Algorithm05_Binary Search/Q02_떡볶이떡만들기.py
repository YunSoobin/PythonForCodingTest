'''
- 문제 해결을 위한 아이디어(이진 탐색, Parametric Search : 최적화 문제를 결정 문제로 바꾸어 해결하는 기법)는 답안과 일치하게 떠올렸다.
- 이진 탐색을 위한 끝점 설정
    ( 나의 답안 : 최댓값 - 1 => 손님이 요청한 떡의 최소 길이가 1cm이므로 )
    ( 답안 예시 : 최댓값 )
- 결괏값(절단기 높이의 최댓값)을 갱신하는 위치를 잘못 설정하여
    ( "최댓값" 키워드를 놓쳐 잘린 떡의 길이와 손님이 요청한 총 길이가 같은 경우만 고려 )
    답안 예시를 참고해 재구현했다.
    ( 잘린 떡의 길이가 손님이 요청한 총 길이보다 길거나 같은 경우 모두 고려 )
'''


import time
start_time = time.time()

def binary_search(start, end, M, riceCake):
    result = 0
    while start <= end:
        height = (start + end) // 2

        total = 0    # 잘린 떡의 길이
        for i in riceCake:
            total += max(0, i - height)

        if total >= M:    # 잘린 떡의 길이가 손님이 요청한 총 길이보다 길거나 같은 경우
            start = height + 1
            result = height
        else:   # 잘린 떡의 길이가 손님이 요청한 총 길이보다 짧은 경우
            end = height - 1

    return result

N, M = map(int, input().split())
riceCake = list(map(int, input().split()))

print(binary_search(0, max(riceCake) - 1, M, riceCake))

end_time = time.time()
print("time: ", end_time - start_time)