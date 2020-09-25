# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

# class Solution:
#     def containsDuplicate(self, nums):
#         mem = set()
#         while nums is not []:
#             number = nums.pop()
#             if number in mem:
#                 return True
#             else :
#                 mem.add(number)
#             # count += 1
#         return False

# mySolution = Solution()

# print(mySolution.containsDuplicate([1,2,4,3,6,1]))

x = [1,2,4,5,6`]
head = 0
tail = -1
print(x)
while (tail * -1) < len(x) -1 //2 -1:
    if tail is 0:
        tail -=1
    
    print(x[head])
    print(x[tail])
    head += 1
    tail -=1