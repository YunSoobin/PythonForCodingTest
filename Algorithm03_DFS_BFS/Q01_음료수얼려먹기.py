'''
- DFS 문제 해결을 위한 아이디어는 (오래 걸렸지만) 답안과 일치하게 떠올렸으나,
    구현에 어려움이 있어 해설을 참조하여 학습한 후 다시 풀어 보았다.
- 상, 하, 좌, 우의 재귀 호출 순서를 고민했는데,
    종료 조건을 정하고 if문 안에 일괄적으로 호출하면 되는 것이다.
- graph[0][0]부터 연결된 노드를 모드 방문한 후 True를 return 한다.
    다음 반복 과정에서 graph[0][0]과 연결된 노드의 visited 리스트에는 True가 저장되어 있으므로 bfs 함수가 실행되지 않는다.
    즉, 연결된 노드들은 True 한 개 만을 반환한다.
'''


import time
start_time = time.time()

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(graph, x, y, visited):
    # 종료 조건
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 0 and not visited[x][y]:    # 구멍이 뚫려 있는 칸, 방문하지 않은 노드
        visited[x][y] = True  # 현재 노드 방문 표시
        bfs(graph, x - 1, y, visited)   # 상
        bfs(graph, x + 1, y, visited)   # 하
        bfs(graph, x, y - 1, visited)   # 좌
        bfs(graph, x, y + 1, visited)   # 우
        # 연결된 노드를 모두 방문한 후 True(1) 반환
        return True

    return False

visited = [[False for _ in range(M)] for _ in range(N)] # 노드 방문 여부

result = 0
for i in range(N):
    for j in range(M):
        result += bfs(graph, i, j, visited)

print(result)

end_time = time.time()
print("time : ", end_time - start_time)