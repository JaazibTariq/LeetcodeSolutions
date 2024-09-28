class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        ans = []
        strs2 = strs.copy()
        hash1 = set()
        hash = {}
        for i in range(len(strs)):
            strs[i] = ''.join(sorted(strs[i]))
        
        for i in range(len(strs)):
            
            if(strs[i] in hash1):
                ans[hash[strs[i]]].append(strs2[i])
            else:
                hash1.add(strs[i])
                hash[strs[i]] = count
                ans.append([strs2[i]])
                count += 1
        return ans

