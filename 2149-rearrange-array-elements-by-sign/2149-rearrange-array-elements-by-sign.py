class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[] #양수 리스트
        negative=[] #음수 리스트
        answer=[]
        #양수, 음수 나누기
        for num in nums:
            if num>0:
                positive.append(num)
            elif num<0:
                negative.append(num)
        #양수, 음수 번갈아 가며 리스트에 삽입
        for i in range(len(nums)//2):
            answer.append(positive[i])
            answer.append(negative[i])
        return answer