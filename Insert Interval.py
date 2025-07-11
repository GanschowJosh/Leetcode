"""Bad solution
def insert(intervals, newInterval):
    newIntervals = []
    flag = False #flag checking if new interval has been considered
    for interval in intervals:
        if interval[1] >= newInterval[0] and interval[1] <= newInterval[1]: #overlaps
            newIntervals.append([min(newInterval[0], interval[0]), max(newInterval[1], interval[1])])
            flag = True
        if newInterval[1] >= interval[0] and newInterval[1] <= interval[1]:
            newIntervals.append([min(newInterval[0], interval[0]), max(newInterval[1], interval[1])])
            flag = True
        else:
            newIntervals.append(interval)
    if not newIntervals or not flag: #handling case of empty intervals or newInterval wasn't used
        newIntervals.append(newInterval)
    #reused code from `Merge Intervals` problem
    newIntervals.sort(key=lambda x: x[0])
    merged = []
    for interval in newIntervals:
        if not merged or merged[-1][1] < interval[0]: #if merged is empty or current interval doesn't overlap
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

print(insert(intervals = [[1,5]], newInterval = [0, 0]))"""

#slightly less bad solution
def insertInterval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge intervals that overlap with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add the merged newInterval
    result.append(newInterval)

    # Add the remaining intervals that come after newInterval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Example usage
intervals = [[1,3], [6,9]]
newInterval = [2,5]
print(insertInterval(intervals, newInterval))
