from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        deq=deque(nums) #deque로 변환
        deq.rotate(k%len(deq)) #오른쪽으로 이동 
        nums[:]=list(deq) #리스트로 변환
        