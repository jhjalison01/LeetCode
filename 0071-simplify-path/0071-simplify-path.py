class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/') # '/'을 기준으로 쪼개기
        while "" in path:
            path.remove("")
        while "." in path: # "."은 현재 폴더를 나타내므로 삭제
            path.remove(".")
        while ".." in path: # ".."은 상위 폴더로 가야하므로 이전 요소도 제거
            idx = path.index("..")
            del path[idx]
            if idx>0:
                del path[idx-1]
        path="/".join(path) # '/'으로 연결하기
        return "/"+path #path는 '/'으로 시작해야한다.