#Given a string s, find the length of the longest substring without duplicate characters.
#
# Example 1: Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:  Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example  3: Input: s = "pwwkew"
# Output: 3
# Explanation: The  answer is "wke", with the length of 3.
# Noticethat the answer must be a substring, "pwke" is a subsequence and not a substring.

class solution:

    def longestsubstring(self,s:str):
        charset=set()
        left_index=0
        res=0
        for right_index in range(0,len(s)):  #Right Index is set to 0 and is iterated from 0which is first location to the length of string
            while s[right_index] in charset: #While iterating if the right character is in the set, we need to remove the left index character and move it to next character the vaue of left_index inside a while loop
                charset.remove(s[left_index])
                left_index+=1
            charset.add(s[right_index]) #ONce duplicate ones are removed and left index is moved, start adding character right to the chaset
            res= max(res,right_index-left_index+1) # max length is calculated by comparing max of existing length wtj R-L+1
        return res

    @staticmethod
    def findSumoftwoNumberInList(numlist:list[int],target:int):

        for i,num in enumerate(numlist):
            print(i,num)
            othernumber=target-num
            for j in range(i+1,len(numlist)):
                if nums[j] == othernumber:
#if othernumber in numlist:
                    print(target-num)
                    #return(i,numlist.index(othernumber)) #does not work for [3,3] target 6 , returns(0,0)instead of 0,1
                    return(i,j)
        return"Target Combination NOT Found"

    @staticmethod
    def findSumoftwoNumberInListOptimized(numlist: list[int], target: int):
        dict_numList={}
        for i, num in enumerate(numlist):
            print(i, num)
            othernumber = target - num
            if othernumber in dict_numList:
                return(dict_numList[othernumber],i)
            dict_numList[num]=i

        return []


#------------------------------------
#FUNCTION TO FIND INDEX OF TWO NUMBERS THAT SUM TO THE REQUIRED TARGET
#
# nums=[2,7,11,15]
# target=26
nums=[3,3]
target=6
#index1=solution.findSumoftwoNumberInList(nums,target)
index1=solution.findSumoftwoNumberInListOptimized(nums,target)
print(index1)

# #---------------------------------------------------------------------------------------------------------------------
# # FUNCTION to GET MAX SUBSTRING
#
# solution_obj=solution()
# max_substringLength=solution_obj.longestsubstring("abcabcbb")
#
# print(f"LongestString length = {max_substringLength}")
