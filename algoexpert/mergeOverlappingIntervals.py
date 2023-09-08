def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda a:a[0])
    ans = [intervals[0]]
    for start, end in intervals[1:]:
        end_cur = ans[-1][1]
        if start> end_cur:
            ans.append([start, end])
        else:
            ans[-1][1] = max(end, end_cur)

    return ans
print(mergeOverlappingIntervals([
    [100, 105],
    [1, 104]
]))
