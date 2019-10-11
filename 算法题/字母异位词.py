class Solution:
    def groupAnagrams(strs) :
        d={}
        for w in strs:
            x=tuple(sorted(list(w)))
            if d.__contains__(x):
                d[x].append(w)
            else:
                d[x]=[w]
        return d.values()
strs= ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution.groupAnagrams(strs))