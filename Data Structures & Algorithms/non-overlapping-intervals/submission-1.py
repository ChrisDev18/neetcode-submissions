class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals by finish time
        intervals.sort(key=lambda x: x[1])
        print(intervals)

        last_end: Optional[int] = None
        total = 0
        
        # go through intervals, removing the ones that conflict
        for start, end in intervals:
            if last_end is None:
                last_end = end
                continue

            if last_end > start:
                total += 1
            else:
                last_end = end
        
        return total