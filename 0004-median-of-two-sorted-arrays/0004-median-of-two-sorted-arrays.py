class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge=[]
        merge= nums1 + nums2
        merge.sort()
        n=len(merge)
        if n %2 == 0:
            med=(merge[(n//2) -1]+merge[n//2])/2
            return med 
        elif n %2 != 0:
            med= merge[(n-1)//2]
            return med    
        