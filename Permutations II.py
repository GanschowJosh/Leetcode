class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = list(nums)
        length_of_iterable = len(nums)

        #base cases
        if length_of_iterable in [0,1]:
            return [nums.copy()]

        permutations = []
        seen_anchors = set()
        for i in range(length_of_iterable):
            current = nums[i]
            if current in seen_anchors:
                continue
            seen_anchors.add(current)
            remaining = nums[:i] + nums[i+1:] #all elements except current one
            #recursively get permutations of the remaining elements
            for p in self.permuteUnique(remaining):
                permutations.append([current] + p) #prepend current to each permutation
        
        return permutations  