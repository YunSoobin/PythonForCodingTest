'''
- 문제 해결을 위한 아이디어(기본 정렬 라이브러리의 Key 사용)는 답안과 일치하게 떠올렸다.
- 학생 정보를 저장하는 방식
    ( 나의 답안 : 입력 받은 문자열 형태 그대로 리스트에 저장,
                학생 성적 비교 시 문자열을 정수형으로 변환 )
    ( 답안 예시 : 문자열 형태로 리스트에 입력 받은 뒤,
                학생 성적만 정수형으로 변환하여 튜플에 저장 )
'''


import time
start_time = time.time()

N = int(input())

# 학생 정보 입력
student = []
for _ in range(N):
    student.append(input().split())

student.sort(key=lambda x:int(x[1]))
# x[1]을 int()형으로 변환하지 않으면
# 성적을 문자열로 인식하여 학생의 성적이 '100'점일 경우 오류 발생

for i in range(N):
    print(student[i][0], end=' ')

end_time = time.time()
print("\ntime : ", end_time - start_time)