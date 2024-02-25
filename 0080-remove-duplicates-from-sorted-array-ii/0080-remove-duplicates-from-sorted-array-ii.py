from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt_dict=defaultdict(int) #초기값 0으로 초기화
        k=0 #인덱스
        for i in range(len(nums)):
            cnt_dict[nums[i]]+=1 #해당 숫자 개수 카운트
            if cnt_dict[nums[i]]<=2: #개수가 2이하일 경우
                nums[k]=nums[i] #해당 숫자를 인덱스에 삽입
                k+=1 #인덱스 1 증가
            else: #개수가 2를 초과할 경우
                continue
        return k