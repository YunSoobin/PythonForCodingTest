'''
- 시뮬레이션 문제 구현에 어려움이 있어 해설을 참조하여 학습한 후 다시 풀어 보았다.
- "일반적으로 direction을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다."
- 한 단계마다 캐릭터의 상태를 출력하며 차근차근 문제를 해결했다. (주석 처리 해 두었다.)
'''


import time
start_time = time.time()

N, M = map(int, input().split())
A, B, d = map(int, input().split())
map_inform = [list(map(int, input().split())) for _ in range(N)]    # 육지(0) / 바다(1) 정보

map_visit = [[0] * M for _ in range(N)]   # 캐릭터의 방문 여부 확인 맵(0: 미방문, 1: 방문)

dx = [-1, 0, 1, 0]  # 행 방향 이동
dy = [0, 1, 0, -1]  # 열 방향 이동

def turn_left():
    global d, turn
    d -= 1  # 회전
    # "list index out of range" 오류 방지
    if d == -1:
        d = 3
    turn += 1

# 현재 위치 방문 표시
map_visit[A][B] = 1

turn = 0    # 캐릭터의 회전 횟수
while True:
    # 캐릭터의 위치 기준 왼쪽 방향 칸
    A += dx[d - 1]
    B += dy[d - 1]
    # print("다음 위치는 ? ", A, B)
    if map_inform[A][B] == 1:    # 왼쪽 방향이 바다인 경우
        # print("저의 왼쪽은 바다입니다. 회전할게요!")
        turn_left()
        # 움직이지 않음
        A -= dx[d]
        B -= dy[d]
        # print("현재 위치와 바라보는 뱡향은 ? ", A, B, d)
    else:   # 왼쪽 방향이 바다가 아닌 경우
        # print("저의 왼쪽은 땅입니다.")
        if map_visit[A][B] == 0:    # 왼쪽 방향이 가보지 않은 칸인 경우
            # print("저의 왼쪽은 방문하지 않았어요. 전진할게요!")
            turn_left()
            map_visit[A][B] = 1 # 한 칸 전진, 방문 표시
            turn = 0
            # print("현재 위치와 바라보는 뱡향은 ? ", A, B, d)
            continue
        else:   # 왼쪽 방향이 가본 칸인 경우
            # print("저의 왼쪽은 방문했어요. 회전할게요!")
            turn_left()
            # 움직이지 않음
            A -= dx[d]
            B -= dy[d]
            # print("현재 위치와 바라보는 뱡향은 ? ", A, B, d)

    if turn == 4:   # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우
        A -= dx[d]
        B -= dy[d]
        # print("다음 위치는 ? ", A, B)
        # print("움직일 수 없습니다.")
        if map_inform[A][B] == 0:   # 뒤쪽이 바다가 아닌 경우
            # print("저의 뒤쪽은 바다가 아니에요. 후진할게요!")
            turn = 0    # 한 칸 후진
            # print("현재 위치와 바라보는 뱡향은 ? ", A, B, d)
            continue
        else:   # 뒤쪽이 바다인 경우
            # print("후진할 수 없어요! 종료합니다.")
            break

count = 0
for i in range(N):
    count += map_visit[i].count(1)
print(count)

end_time = time.time()
print("time : ", end_time - start_time)
