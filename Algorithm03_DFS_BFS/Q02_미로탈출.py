'''
- 문제 해결을 위한 아이디어
    ( 나의 답안 : stack 사용 )
    ( 답안 예시 : queue 사용 )
- 최단 거리 구하는 방식
    ( 나의 답안 : BFS 실행 횟수 + 1 )
    ( 답안 예시 : 노드 값 변경 )
- 동빈이가 이동할 방향
    ( 나의 답안 : 두 뱡향으로 설정 - 하, 우 )
    ( 답안 예시 : 네 방향으로 설정 - 상, 하, 좌, 우 )
'''


import time
start_time = time.time()

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

def bfs(graph, i, j):
    global result   # 최소 이동 칸의 개수
    result = 0

    # "최소" 이동 칸의 개수를 구하는 것이므로 i, j 모두 양수 방향으로만 이동 가능
    if i + 1 < N and graph[i + 1][j] == 1:  # 하로 탐색
        bfs(graph, i + 1, j)
        result += 1

    if j + 1 < M and graph[i][j + 1] == 1:  # 우로 탐색
        bfs(graph, i, j + 1)
        result += 1

bfs(graph, 0, 0)

print(result + 1)   # "+ 1"은 시작 칸 포함을 의미

end_time = time.time()
print("time : ", end_time - start_time)