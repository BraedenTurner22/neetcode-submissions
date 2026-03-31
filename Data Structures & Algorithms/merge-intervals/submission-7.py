class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        response = [intervals[0]]

        for start, end in intervals:
            lastEnd = response[-1][1]

            if start <= lastEnd:
                response[-1][1] = max(lastEnd, end)
            else:
                response.append([start, end])
            
        return response