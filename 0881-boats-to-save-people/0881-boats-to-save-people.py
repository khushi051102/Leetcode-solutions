class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        lo,hi=0,len(people)-1
        count=0
        while lo<=hi:
            if people[lo]+people[hi]<=limit:
                lo+=1
            hi-=1
            count+=1
        return count
