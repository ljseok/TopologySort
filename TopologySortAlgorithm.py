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

    while q: # 큐가 빌 때까지 반복
        now = q.popleft() # 큐에서 원소를 꺼낸다
        result.append(now)

        for i in graph[now]: # 해당 원소와 연결된 노드중에서
            indgree[i] -= 1 # 진입차수를 1만큼 뺀다

            if indgree[i] == 0: # 새롭게 진입차수가 0이되는 노드를
                q.append(i) # 큐에 삽입

    for i in result:
        print(i, end=' ')

topology_sort()