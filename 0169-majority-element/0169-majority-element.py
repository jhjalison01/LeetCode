from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int) #딕셔너리 선언
        result=[]  
        for i in range(len(nums)):
            cnt[nums[i]]+=1 #횟수 1 카운트
            if cnt[nums[i]]>len(nums)/2: #카운트가 리스트 길이/2 보다 클 경우
                result.append(nums[i])
        return max(result) #result 중 가장 큰 값 리턴


        
        