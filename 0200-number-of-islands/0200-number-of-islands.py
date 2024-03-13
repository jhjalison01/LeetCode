from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs 구현
        def bfs(x,y):
            q=deque()
            q.append((x,y))
            while q:
                x,y=q.popleft()
                #상하좌우 탐색
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    #범위 내에 있고 land일 경우
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny]=="1":
                        grid[nx][ny]="-1" #탐색했음을 표시
                        q.append((nx,ny)) #큐에 넣기
        
        answer=0
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        n=len(grid)
        m=len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    answer+=1 #island의 개수 증가
                    bfs(i,j)
        return answer