class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = sorted(set(nums))
        for i in range(len(st)):
            nums[i] = st[i]
        for j in range(i+1,len(nums)):
            nums[j] = "_"
        return len(st)