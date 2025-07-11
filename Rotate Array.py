class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
                
        #reverse array
        self.reverse(nums, 0, n-1)

        #reverse first k elements
        self.reverse(nums, 0, k-1)

        #reverse the rest of the elements
        self.reverse(nums, k, n-1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1