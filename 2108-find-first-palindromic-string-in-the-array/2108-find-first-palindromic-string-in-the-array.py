class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            #word 길이가 1일 경우 palindromic string임
            if len(word)==1:
                return word
            #중간 위치 찾기
            mid=len(word)//2
            for i in range(mid):
                #대칭 되는 값이 같지 않을 경우
                if word[i] != word[len(word)-i-1]:
                    break
                else: #대칭 되는 값이 같을 경우
                    if i==mid-1: #모든 대칭 되는 값이 같을 경우
                        return word #첫 palindromic string 리턴
        #palindromic string이 없을 경우 "" 리턴
        return ""