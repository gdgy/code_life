#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 9:45
# @Author  : shaoyong_li
# @Site    : 
# @File    : max_array.py

class Solution:
    # @param {int[]} nums1 an integer array of length m with digits 0-9
    # @param {int[]} nums2 an integer array of length n with digits 0-9
    # @param {int} k an integer and k <= m + n
    # @return {int[]} an integer array
    def maxNumber(self, nums1, nums2, k):
        # Write your code here
        def getMax(nums,x):
            ans=[]
            size=len(nums)
            for i in range(size):
                while ans and len(ans)+size-i>x and ans[-1]<nums[i]:
                    ans.pop()
                if len(ans)<x:
                    ans+=nums[i],
            return ans

        def merge(nums1,nums2):
            ans=[]
            while nums1 or nums2:
                if nums1>nums2:
                    ans+=nums1[0],
                    nums1=nums1[1:]
                else:
                    ans+=nums2[0],
                    nums2=nums2[1:]
            return ans

        len1,len2=len(nums1),len(nums2)
        res=[]
        for i in range(max(0,k-len2),min(k,len1)+1):
            tmp=merge(getMax(nums1,i),getMax(nums2,k-i))
            res=max(tmp,res)
        return res

if __name__ == '__main__':
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 10, 5, 8, 3]
    k = 5
    so = Solution()
    print (so.maxNumber(nums1, nums2, 5))