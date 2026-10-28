class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums) #fill output array with 1s temporarily of size nums


        #create a prefix and suffix, one with each loop

        prefix = 1
        
        for i in range(len(nums)):
            output[i] = prefix # store the product in output
            prefix *= nums[i]  #then update the product


        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *=suffix
            suffix *= nums[i]

        return output
            
            







    


