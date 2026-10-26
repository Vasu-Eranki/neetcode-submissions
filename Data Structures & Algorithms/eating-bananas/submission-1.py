class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left =1 
        right = max(piles)
        min_hours = max(piles)
        while(left<=right):
            mid = left + (right-left)//2
            predicted_h = sum([math.ceil(i/mid) for i in piles])
            print(mid,predicted_h)
            if(predicted_h>h):
                left = mid+1
            else:
                right = mid-1
                min_hours = min(min_hours,mid)
        return min_hours


        

        