class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        n=len(prices)
        left=0 #사는 날짜
        right=1 #파는 날짜
        while right<n:
            current_profit=prices[right]-prices[left] #현재 이익
            if prices[left]<prices[right]: #이익이 날 경우
                max_profit = max(current_profit,max_profit) #최대 이익 저장
            else:
                left=right
            right+=1
        return max_profit

        