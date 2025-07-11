def merge(intervals):
    intervals.sort(key=lambda x: x[0]) #sorting based on start time

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]: #if merged is empty or current interval doesn't overlap
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))