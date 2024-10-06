def productExceptSelf(nums):
    n = len(nums)
    nuls = 0
    prod = 1
    res = [0] * n
    
    for i in nums:
        if i == 0:
            nuls += 1
        else:
            prod *= i
        
    if nuls >= 2:
        return res
    
    for i, el in enumerate(nums):
        if nuls == 1:
            if el == 0:
                res[i] = prod
        else:
            res[i] = prod // el       
        
    return res



r1 = productExceptSelf([1,2,3,4])
r2 = productExceptSelf([-1,1,0,-3,3])
