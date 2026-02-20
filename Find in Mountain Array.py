# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        cache={}
        def get(i):
            if i in cache: return cache[i]
            c=mountainArr.get(i)
            cache[i]=c
            return c
        length=mountainArr.length()
        R=length-1
        L=0
        #first find peak
        while L<R:
            mid=L+(R-L)//2
            el=get(mid)
            rightel=get(mid+1)
            if el<rightel:
                L=mid+1
            else:
                R=mid
        #now mid should be peak
        peak=L
        el=get(peak)
        if el < target: return -1 # peak isn't even greater than target, can't possibly be in mountain
        if el==target: return peak
        #now gotta binary search from left to peak
        L=0
        R=peak-1
        while L<=R:
            mid=L+(R-L)//2
            el=get(mid)
            if el==target: return mid
            if el>target:
                R=mid-1
            else:
                L=mid+1
        #now search right side
        L=peak+1
        R=length-1
        while L<=R:
            mid=L+(R-L)//2
            el=get(mid)
            if el==target:return mid
            if el>target:
                L=mid+1
            else:
                R=mid-1
        
        #if we got here, we didnt find it
        return -1