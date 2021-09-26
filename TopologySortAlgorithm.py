from collections import deque

v,e = map(int,input().split()) # v = 노드갯수 , e = 간선 갯수
indgree = [0] * (v+1) # 진입차수를 0으로 초기화
graph = [[]for i in range(v+1)] # 노드의 간선정보를 담고있는 연결리스트를 초기화

for _ in range(e): # 모든 간선의 정보를 입력받기
    a,b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동이 가능하다
    indgree[b] += 1

def topology_sort(): # 위상정렬 함수 정의
    result = [] # 결과값
    q = deque()

    for i in range(1, v+1):
        if indgree[i] == 0: # 진입차수가 0인 노드를
            q.append(i) # 큐에 삽입
