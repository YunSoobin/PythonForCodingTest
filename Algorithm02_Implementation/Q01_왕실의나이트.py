'''
- 문제 해결을 위한 아이디어는 답안과 일치하게 떠올렸다.
- 문자열 입력 및 저장 방식
    ( 나의 답안 : list 형태로 입력 받아 원소 전체를 한 번에 형 변환 )
    ( 답안 예시 : 문자열 형태로 입력 받아 원소 하나씩 형 변환 )
- 변수 선언 방식
    ( 나의 답안 : dx, dy 리스트를 선언하여 이동할 방향 설정 )
    ( 답안 예시 : 튜플을 원소로 갖는 step 리스트를 선언하여 이동할 방향 설정 )
'''


import time
start_time = time.time()

now = list(input())
now[0]=ord(now[0])-96   # 문자를 아스키코드로 변환하고(ord 함수 사용), a의 값을 1로 설정(소문자 a의 아스키코드 = 97)
now = list(map(int, now))   # 리스트 now의 모든 원소를 int 타입으로 변환
now.reverse()   # 리스트 now를 [행, 열] 형태로 바꾸기 위함

dx = [-1, -1, 1, 1, -2, -2, 2, 2]   # 행 이동
dy = [-2, 2, -2, 2, -1, 1, -1, 1]   # 열 이동

count = 0   # 나이트가 이동할 수 있는 경우의 수
for i in range(8):
    nx = now[0] + dx[i]
    ny = now[1] + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:   # 나이트가 8 * 8 좌표 평면 안에 있는 경우
        count += 1

print(count)

end_time = time.time()
print("time : ", end_time - start_time)