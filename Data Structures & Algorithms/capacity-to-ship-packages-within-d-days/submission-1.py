class Solution:
    def calculate_number_of_days(self,weights:List[int],max_weight:int)->int:
        count = 0
        cumSum = 0 
        for i in weights:
            cumSum+=i
            if(cumSum>max_weight):
                count+=1
                cumSum =i 
            elif(cumSum==max_weight):
                count+=1
                cumSum=0
        return count+bool(cumSum)
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = min_weight=sum(weights)
        while(left<=right):
            mid = left + (right-left)//2
            number_of_days = self.calculate_number_of_days(weights,mid)
            if number_of_days<=days:
                min_weight = min(min_weight,mid)
                right = mid-1
            else:
                left = mid+1
        return min_weight
        

        