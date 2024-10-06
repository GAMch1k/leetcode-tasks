def groupAnagrams(strs):
    res = {}
    
    for i in strs:
        k = "".join(sorted(i))
        
        if k in res: res[k].append(i); continue
        res[k] = [i]
    
    return list(res.values())
    
r = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))