class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for a in range(k):
            for b in range(len(nums) - (a + 1)):
                if nums[b] > nums[b + 1]:
                    nums[b], nums[b + 1] = nums[b + 1], nums[b]
        return nums[len(nums) - k]
