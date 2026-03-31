import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        temp = self.nums
        heapq.heapify(temp)

        diff = len(temp) - self.k
        while diff > 0:
            heapq.heappop(temp)
            diff -= 1
        return temp[0]

