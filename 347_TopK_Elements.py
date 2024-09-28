class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        store = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n,c in count.items():
            store[c].append(n)
        ans = []
        for i in range(len(nums), 0, -1):
            if((store[i] != []) and len(ans) < k ):
                if (len(store[i]) >1):
                    for j in range(len(store[i])):
                        if (len(ans) < k):
                            ans.append(store[i][j])
                else:
                    ans.append(store[i][0])
        return ans
