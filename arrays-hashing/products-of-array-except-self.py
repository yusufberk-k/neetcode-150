# Product of Array Except Self
# status: hint | retry: -
# note: missed that output[i] = left product * right product, got stuck on division
# suff is filled in reverse: suff[k] = product of last k elements, hence suff[n-1-i]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = [1]
        pref_product = 1
        suff_product = 1
        products = []
        for i in range(1,len(nums)):
            pref_product *= nums[i-1]
            
            pref.append(pref_product)

        for i in range (len(nums)-2, -1, -1):
            suff_product *= nums[i+1]
            suff.append(suff_product)


        for i in range(0, len(nums)):
            products.append(pref[i]*suff[len(nums)-1-i])

        return products
