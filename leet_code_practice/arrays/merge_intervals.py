from sympy import intervals


Intervals = [[1,3],[2,6],[8,10],[15,18]]


# def merge(intervals):
#         intervals.sort(key=lambda x:x[0])
#         curr = intervals[0]
#         merge = []
#         for i in range(1,len(intervals)):
#             if curr[1]>=intervals[i][0]:
#                 curr[1] = max(curr[1],intervals[i][1])
#             else:
#                 merge.append(curr)
#                 curr = intervals[i]
#         merge.append(curr)
#         return merge

# print(merge(Intervals))




def merge1(intervals):
    intervals.sort(key = lambda x: x[0])
    res = []
    res.append(intervals[0])
    for i in range(1,len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            if intervals[i][1] >= res[-1][1]:
                res[-1][1] = intervals[i][1]
        else:
            res.append(intervals[i])
    return res
    
print(merge1(Intervals))


