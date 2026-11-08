class LogSystem:

    def __init__(self):
        self.hashmap = {}

    def put(self, id: int, timestamp: str) -> None:
        self.hashmap[id] = timestamp

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        hashmap = self.hashmap
        if granularity=="Year":
            start_year = int(start[:4])
            end_year = int(end[:4])
            
            hashmap = [k for k,v in hashmap.items() if int(v[:4])>=start_year and int(v[:4])<=end_year]
        elif granularity=="Month":
            start_month = start[:7]
            end_month = end[:7]
            hashmap = [k for k,v in hashmap.items() if v[:7]>=start_month and v[:7]<=end_month]
        elif granularity=="Day":
            start_day = start[:10]
            end_day = end[:10]
            hashmap = [k for k,v in hashmap.items() if v[:10]>=start_day and v[:10]<=end_day]
        elif granularity=="Hour":
            start_hour = start[:13]
            end_hour = end[:13]
            hashmap = [k for k,v in hashmap.items() if v[:13]>=start_hour and v[:13]<=end_hour]
        elif granularity=="Minute":
            start_minute = start[:16]
            end_minute = end[:16]
            hashmap = [k for k,v in hashmap.items() if v[:16]>=start_minute and v[:16]<=end_minute]
        elif granularity=="Second":
            start_second = start[:19]
            end_second = end[:19]
            print(start_second,end_second)
            hashmap = [k for k,v in hashmap.items() if v[:19]>=start_second and v[:19]<=end_second]
        return hashmap

        
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
