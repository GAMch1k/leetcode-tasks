def containsDuplicate(nums):
    nums.sort()
    s = list(set(nums))
    s.sort()
    return s != nums


print(containsDuplicate([1,5,-2,-4,0]))
# print(containsDuplicate([1,2,3,4]))