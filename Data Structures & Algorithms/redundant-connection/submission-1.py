class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            self.parent[i] = i
    def find(self,n):
        if n!=self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    def union(self,n1,n2):
        parent_of_n1 =self.find(n1)
        parent_of_n2 = self.find(n2)
        if parent_of_n1==parent_of_n2:
            return False
        
        rank_of_p1 = self.rank[parent_of_n1]
        rank_of_p2 = self.rank[parent_of_n2]
        if rank_of_p1>rank_of_p2:
            self.parent[parent_of_n2] = parent_of_n1
        elif rank_of_p1<rank_of_p2:
            self.parent[parent_of_n1] = parent_of_n2
        else:
            self.parent[parent_of_n1] = parent_of_n2
            self.rank[parent_of_n2]+=1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionfind = UnionFind(len(edges))
        duplicateedges = None
        for source,destination in edges:
            result = unionfind.union(source,destination)
            if not result:
                duplicateedges = [source,destination]
        return duplicateedges






        