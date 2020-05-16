from heapq import heappop, heappush
class Solution:
    def solve(self, trips, capacity):
        # Write your code here
        start,end,passengers = list(zip(*trips))
        x = 0
        dropoff = []
        for i in range(len(start)):
            while dropoff and dropoff[0][0] <= start[i]:
                x -= dropoff[0][1]
                heappop(dropoff)
            x += passengers[i]
            if x > capacity:
                return False
            heappush(dropoff, (end[i],passengers[i]))
        return True