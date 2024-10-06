def topKFrequent(nums, k):
    s = set(nums)
    res = {}
    
    for i in s:
        res[i] = nums.count(i)
    
    return list(dict(sorted(res.items(), key=lambda x: x[1], reverse=True)))[:k]
    # return sorted(res)[:k]
    # return sorted(res.values(), reverse=True)
    return res

r1 = topKFrequent([-1,-1,-1,-1,-1,1,1,1,2,2,3], 2)
r2 = topKFrequent([1], 1)
r3 = topKFrequent([4,1,-1,2,-1,2,3], 2)
